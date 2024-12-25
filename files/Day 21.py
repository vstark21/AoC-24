from tqdm import tqdm
import numpy as np
import time
from queue import PriorityQueue
from collections import defaultdict

input_file = open("input.txt", "r")
lines = input_file.readlines()
codes = [line.strip() for line in lines]

DIR_VALUES = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def get_shortest_typing_path(
    start,
    board,
    target_code
):
    # board: nxm matrix, [[1, 2], [3, 4]]
    # target_code: string "123"
    # start: tuple (x, y)

    char_pos = defaultdict(tuple)
    for i in range(len(board)):
        for j in range(len(board[i])):
            char_pos[str(board[i][j])] = (i, j)

    def move(start, end):
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        ans = ""
        if dy > 0:
            ans += ">" * dy
        elif dy < 0:
            ans += "<" * (-dy)
        if dx > 0:
            ans += "v" * dx
        elif dx < 0:
            ans += "^" * (-dx)
        return ans + 'A'

    idx = 0
    path = ""
    cur_pos = start
    while idx < len(target_code):
        path += move(cur_pos, char_pos[target_code[idx]])
        cur_pos = char_pos[target_code[idx]]
        idx += 1

    return path


num_keypad = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ["X", 0, "A"]
]
directional_keypad = [
    ['X', '^', 'A'],
    ['<', 'v', '>'],
]
ans = 0
GLOBAL_VIS = defaultdict(lambda: -1)

def solve():
    def rec(keypad, code, depth, start):
        if depth == TOTAL_DEPTH:
            return len(code)
        

        char_pos = defaultdict(tuple)
        for i in range(len(keypad)):
            for j in range(len(keypad[i])):
                char_pos[str(keypad[i][j])] = (i, j)

        def get_possible_paths(start, end):
            dx = end[0] - start[0]
            dy = end[1] - start[1]

            path1 = ""
            if dy > 0:
                path1 += ">" * dy
            elif dy < 0:
                path1 += "<" * (-dy)
            if dx > 0:
                path1 += "v" * dx
            elif dx < 0:
                path1 += "^" * (-dx)
            path2 = path1[::-1]

            return path1 + 'A', path2 + 'A'
        
        def is_okay(path1, start):
            cur_pos = start
            for ch in path1[:-1]:
                cur_pos = (cur_pos[0] + DIR_VALUES[ch][0], cur_pos[1] + DIR_VALUES[ch][1])
                if keypad[cur_pos[0]][cur_pos[1]] == 'X':
                    return False
            return True

        
        idx = 0
        cur_pos = start
        min_len = 0
        while idx < len(code):
            path1, path2 = get_possible_paths(cur_pos, char_pos[code[idx]])

            cur_len = float('inf')

            if is_okay(path1, cur_pos):
                if GLOBAL_VIS[(path1, depth)] == -1:
                    GLOBAL_VIS[(path1, depth)] = rec(directional_keypad, path1, depth + 1, (0, 2))
                
                cur_len = min(cur_len, GLOBAL_VIS[(path1, depth)])
            if is_okay(path2, cur_pos):
                if GLOBAL_VIS[(path2, depth)] == -1:
                    GLOBAL_VIS[(path2, depth)] = rec(directional_keypad, path2, depth + 1, (0, 2))
                cur_len = min(cur_len, GLOBAL_VIS[(path2, depth)])
                                
            min_len += cur_len
            cur_pos = char_pos[code[idx]]
            idx += 1

        return min_len

    TOTAL_DEPTH = 26 # 3 and 26 for part 1 and 2
    ans = 0
    for code in codes:
        GLOBAL_VIS.clear()
        cur_ans = rec(num_keypad, code, 0, (3, 2))
        ans = int(code[:-1]) * cur_ans + ans

    print(ans)

solve()