from tqdm import tqdm
import numpy as np
from queue import PriorityQueue
from collections import defaultdict
from collections import deque

input_file = open("input.txt", "r")
lines = input_file.readlines()
lines.append("\n")
cur_block = []
keys = []
locks = []
for line in lines:
    line = line.strip()
    if line == "":
        if cur_block[0][0] == '#':
            locks.append(cur_block)
        else:
            keys.append(cur_block)
        cur_block = []
        continue
    cur_block.append([el for el in line])

def block_to_num(cur_block, dx=-1):# dx: 0 for key, -1 for lock
    arr = [0] * 5
    for i in range(1, 6):
        for j in range(5):
            arr[j] += (cur_block[i][j] == '#')

    for j in range(5):
        arr[j] += cur_block[dx][j] == '#'

    return arr


nlocks = []
nkeys = []
for lock in locks:
    nlocks.append(block_to_num(lock, -1))

for key in keys:
    nkeys.append(block_to_num(key, 0))


def is_compatible(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True
        
ans = 0
for key in nkeys:
    for lock in nlocks:
        if is_compatible(key, lock):
            ans += 1

print(ans)
