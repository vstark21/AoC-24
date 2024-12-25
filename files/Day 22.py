from tqdm import tqdm
import numpy as np
from queue import PriorityQueue
from collections import defaultdict
from collections import deque

input_file = open("input.txt", "r")
lines = input_file.readlines()


def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def process(secret_number):
    """
    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    """

    secret_number = mix(secret_number, secret_number * 64)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, secret_number // 32)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, secret_number * 2048)
    secret_number = prune(secret_number)

    return secret_number

def solve1():
    sec_nums = [int(line.strip()) for line in lines]
    ans = 0
    for sec in sec_nums:
        cur = sec

        for _ in range(2000):
            cur = process(cur)

        ans += cur

    print(ans)

def solve2():
    sec_nums = [int(line.strip()) for line in lines]
    ans = 0
    dic = defaultdict(int)

    for ti, sec in tqdm(enumerate(sec_nums), total=len(sec_nums)):
        cur = sec
        cur_ts = []

        for _ in range(2000):
            cur_ts.append(cur % 10)
            cur = process(cur)

        cur_ts.append(cur % 10)
        
        ch_ts = deque(maxlen=4)
        vis = set()
        for i in range(1, len(cur_ts)):
            ch_ts.append(cur_ts[i] - cur_ts[i - 1])
            
            if i > 3:
                last_4 = tuple(ch_ts)
                if not last_4 in vis:
                    vis.add(last_4)
                    dic[last_4] += cur_ts[i]
        

    ans = max(dic.values())
    
    for el in dic:
        if dic[el] == ans:
            print(el, ans)

# solve1()
solve2()
