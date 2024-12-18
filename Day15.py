from tqdm import tqdm
import numpy as np
import time

input_file = open("input.txt", "r")
lines = input_file.readlines()
grid = []
while 1:
    line = lines.pop(0)
    if line == "\n":
        break
    grid.append(list(line.strip()))

actions = ""
for line in lines:
    if line != "\n":
        actions += line.strip()

def move(x, y, cur_dir, grid, token):
    nx, ny = x + cur_dir[0], y + cur_dir[1]
    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
        return (x, y), False
    if grid[nx][ny] == "#":
        return (x, y), False
    
    if grid[nx][ny] == "O":
        if move(nx, ny, cur_dir, grid, 'O')[-1]:
            grid[nx][ny] = token
            return (nx, ny), True
    elif grid[nx][ny] == ".":
        grid[nx][ny] = token
        return (nx, ny), True
    return (x, y), False
    


def execute_action(grid, action, pos):
    cur_dir = None
    if action == '>':
        cur_dir = [0, 1]
    elif action == '<':
        cur_dir = [0, -1]
    elif action == '^':
        cur_dir = [-1, 0]
    else:
        cur_dir = [1, 0]
    
    npos, ret = move(pos[0], pos[1], cur_dir, grid, "@")
    if ret:
        grid[pos[0]][pos[1]] = "."
        pos = npos
    
    return pos

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print()

def calculate_distances(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                ans += 100 * i + j

    return ans

def solve(grid, actions):
    spos = [0, 0]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                spos = [i, j]
                break
        else:
            continue
        break

    for action in tqdm(actions):
        spos = execute_action(grid, action, spos)
    
    print_grid(grid)
    
    ans = calculate_distances(grid)
    print(ans)


def execute_action2(grid, action, pos):
    cur_dir = None
    if action == '>':
        cur_dir = [0, 1]
    elif action == '<':
        cur_dir = [0, -1]
    elif action == '^':
        cur_dir = [-1, 0]
    else:
        cur_dir = [1, 0]
    
    npos, ret = move2(pos[0], pos[1], cur_dir, grid, "@")
    if ret:
        grid[pos[0]][pos[1]] = "."
        pos = npos
    
    return pos

def move2(x, y, cur_dir, grid, token):
    nx, ny = x + cur_dir[0], y + cur_dir[1]
    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
        return (x, y), False
    if grid[nx][ny] == "#":
        return (x, y), False
    
    if grid[nx][ny] == "[]":
        if move2(nx, ny, cur_dir, grid, 'O')[-1]:
            grid[nx][ny] = token
            return (nx, ny), True
    elif grid[nx][ny] == ".":
        grid[nx][ny] = token
        return (nx, ny), True
    return (x, y), False


def solve2(grid, actions):
    # updating grid according to ps2
    new_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                row.extend(['@', '.'])
            elif grid[i][j] == 'O':
                row.extend(['[', ']'])
            else:
                row.extend([grid[i][j]] * 2)

        new_grid.append(row)
    
    grid = new_grid

    spos = [0, 0]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                spos = [i, j]
                break
        else:
            continue
        break

    for action in tqdm(actions):
        spos = execute_action2(grid, action, spos)
    
    print_grid(grid)
    
    ans = calculate_distances(grid)
    print(ans)



solve2(grid, actions)
