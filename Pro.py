from tqdm import tqdm
import numpy as np
import time

input_file = open("input.txt", "r")
lines = input_file.readlines()
lines = [line.strip('\n') for line in lines]
lines = list(filter(lambda a: len(a) > 0, lines))

class Robot:
    def __init__(self, line):
        # line: p=0,4 v=3,-3
        self.x = int(line.split(' ')[0].split('=')[1].split(',')[0])
        self.y = int(line.split(' ')[0].split('=')[1].split(',')[1])
        self.vx = int(line.split(' ')[1].split('=')[1].split(',')[0])
        self.vy = int(line.split(' ')[1].split('=')[1].split(',')[1])
    
    def move(self, limx, limy):
        self.x = (self.x + self.vx) % limx
        self.y = (self.y + self.vy) % limy

    def __str__(self):
        return "Robot at ({}, {}) with velocity ({}, {})".format(self.x, self.y, self.vx, self.vy)

def solve(arr):
    robots = [Robot(line) for line in arr]
    LIMX = 101
    LIMY = 103
    TIME = 100

    for _ in range(100):
        for robot in robots:
            robot.move(LIMX, LIMY)

    grid = np.zeros((LIMY, LIMX), dtype=int)
    for robot in robots:
        grid[robot.y, robot.x] += 1

    # for every quadrant count the number of robots
    quandrant_width = LIMX // 2
    quandrant_height = LIMY // 2

    def count_robots(grid, sx, sy, qw, qh):
        count = 0
        for i in range(sy, sy + qh):
            for j in range(sx, sx + qw):
                count += grid[i, j]
        return count

    ans = 1
    ans *= count_robots(grid, 0, 0, quandrant_width, quandrant_height)
    ans *= count_robots(grid, LIMX-quandrant_width, 0, quandrant_width, quandrant_height)
    ans *= count_robots(grid, 0, LIMY-quandrant_height, quandrant_width, quandrant_height)
    ans *= count_robots(grid, LIMX-quandrant_width, LIMY-quandrant_height, quandrant_width, quandrant_height)

    print(ans)

def analyze(robots):
    grid = np.zeros((103, 101), dtype=int)
    for robot in robots:
        grid[robot.y, robot.x] += 1

    total_count = len(robots)
    adj_count = 0
    for robot in robots:
        # check all dirs for other robots
        x = robot.x
        y = robot.y
        if x > 0 and grid[y, x-1] > 0:
            adj_count += 1
        elif x < 100 and grid[y, x+1] > 0:
            adj_count += 1
        elif y > 0 and grid[y-1, x] > 0:
            adj_count += 1
        elif y < 102 and grid[y+1, x] > 0:
            adj_count += 1
        elif x > 0 and y > 0 and grid[y-1, x-1] > 0:
            adj_count += 1
        elif x < 100 and y < 102 and grid[y+1, x+1] > 0:
            adj_count += 1
        elif x > 0 and y < 102 and grid[y+1, x-1] > 0:
            adj_count += 1
        elif x < 100 and y > 0 and grid[y-1, x+1] > 0:
            adj_count += 1
        
    return round(adj_count / total_count, 2)


def solve2(arr):
    robots = [Robot(line) for line in arr]
    LIMX = 101
    LIMY = 103
    TIME = 10000
    threshold = .60

    for t in tqdm(range(TIME)):
        for robot in robots:
            robot.move(LIMX, LIMY)

        adj = analyze(robots)
        if adj > threshold:
            grid = np.zeros((LIMY, LIMX), dtype=int)
            for robot in robots:
                grid[robot.y, robot.x] += 1
            
            for i in range(LIMY):
                for j in range(LIMX):
                    if grid[i, j] > 0:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
            print(adj, t + 1)

        



solve2(lines)