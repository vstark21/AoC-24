from tqdm import tqdm
import numpy as np
import time
from queue import PriorityQueue

input_file = open("input.txt", "r")
lines = input_file.readlines()

dic = set(w.strip(',') for w in lines[0].split())
max_len = max([len(el) for el in dic])
words = [w.strip() for w in lines[2:]]
# print(words)

def is_possible(word, idx, dic, vis):
    if idx >= len(word):
        return True
    
    if vis[idx]:
        return False

    c = ''
    ans = False
    for i in range(idx, len(word)):
        c += word[i]
        if c in dic:
            if is_possible(word, i + 1, dic, vis):
                ans = True
                break
        
        if len(c) >= max_len:
            ans = False
            break
    
    vis[idx] = True
    return ans

def count_possible(word, idx, dic, count):
    if idx >= len(word):
        return 1

    if count[idx] != -1:
        return count[idx]

    c = ''
    ans = 0
    for i in range(idx, len(word)):
        c += word[i]
        if c in dic:
            ans += count_possible(word, i + 1, dic, count)

        if len(c) >= max_len:
            break
    
    count[idx] = ans
    return ans
    

def solve1():
    count = 0
    for word in tqdm(words):
        vis = [False] * len(word)
        if is_possible(word, 0, dic, vis):
            count += 1
    print(count)

def solve2():
    count = 0
    for word in tqdm(words):
        vis = [-1] * len(word)
        count += count_possible(word, 0, dic, vis)
    print(count)

# solve1()
solve2()
