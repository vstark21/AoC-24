from tqdm import tqdm
import numpy as np
import time
from queue import PriorityQueue

input_file = open("input.txt", "r")
lines = input_file.readlines()
grid = []
while lines:
    line = lines.pop(0)
    if line == "\n":
        break
    grid.append(list(line.strip()))

class Node:
    def __init__(self, x, y, dx, dy, dist, parent=None):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.dist = dist
        self.p=parent

    def __lt__(self, other):
        return self.dist < other.dist
    
def get_dir_idx(dir_):
    if dir_ == (0, 1):
        return 0
    elif dir_ == (1, 0):
        return 1
    elif dir_ == (0, -1):
        return 2
    elif dir_ == (-1, 0):
        return 3

def solve(grid):
    start = (0, 0)
    end = (0, 0)
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    print(start, end)
    pq = PriorityQueue()
    pq.put(Node(start[0], start[1], 0, 1, 0))
    dist_score = np.full((n, m, 4), -1)


    while not pq.empty():
        node = pq.get()
        if dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))] != -1 and node.dist >= dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))]:
            continue

        dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))] = node.dist
        if (node.x, node.y) == end:
            ans = node.dist
            break

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (dx, dy) == (-node.dx, -node.dy):
                continue
            elif (dx, dy) == (node.dx, node.dy):
                new_node = Node(node.x + dx, node.y + dy, dx, dy, node.dist + 1)
            else:
                new_node = Node(node.x, node.y, dx, dy, node.dist + 1000)
                

            if new_node.x < 0 or new_node.x >= n or new_node.y < 0 or new_node.y >= m or grid[new_node.x][new_node.y] == "#":
                continue
            pq.put(new_node)
    
    print(ans)
        
def solve2(grid):
    start = (0, 0)
    end = (0, 0)
    n = len(grid)
    m = len(grid[0])

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)

    print(start, end)
    pq = PriorityQueue()
    pq.put(Node(start[0], start[1], 0, 1, 0, Node(-1,-1,-1,-1,-1)))
    dist_score = np.full((n, m, 4), -1)
    parent = [[[set() for _ in range(4)] for _ in range(m)] for _ in range(n)]

    paths = []
    ans = float('inf')

    while not pq.empty():
        node = pq.get()
        if dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))] != -1 and node.dist > dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))]:
            continue

        if node.dist < dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))]:
            parent[node.x][node.y][get_dir_idx((node.dx, node.dy))] = set()

        parent[node.x][node.y][get_dir_idx((node.dx, node.dy))].add((node.p.x, node.p.y, node.p.dx, node.p.dy))

        dist_score[node.x][node.y][get_dir_idx((node.dx, node.dy))] = node.dist
        if (node.x, node.y) == end and node.dist <= ans:
            ans = min(ans, node.dist)
            paths.append((node.x, node.y, node.dx, node.dy, node.dist))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (dx, dy) == (-node.dx, -node.dy):
                continue
            elif (dx, dy) == (node.dx, node.dy):
                new_node = Node(node.x + dx, node.y + dy, dx, dy, node.dist + 1, Node(node.x, node.y, node.dx, node.dy, node.dist))
            else:
                new_node = Node(node.x, node.y, dx, dy, node.dist + 1000, Node(node.x, node.y, node.dx, node.dy, node.dist))
                

            if new_node.x < 0 or new_node.x >= n or new_node.y < 0 or new_node.y >= m or grid[new_node.x][new_node.y] == "#":
                continue
            pq.put(new_node)
    
    # print(ans)
    # print(paths)

    seats = [[0 for _ in range(m)] for _ in range(n)]

    def backtrack(x, y, dx, dy, parent, seats):
        seats[x][y] += 1
        if (x, y) == start:
            return
        for px, py, pdx, pdy in parent[x][y][get_dir_idx((dx, dy))]:
            backtrack(px, py, pdx, pdy, parent, seats)
            

    for path in paths:
        x, y, dx, dy, dist = path
        if dist != ans:continue

        backtrack(x, y, dx, dy, parent, seats)

    # for i in range(n):
    #     for j in range(m):
    #         print(seats[i][j], end=" ")
    #     print()

    final_ans = 0
    for i in range(n):
        for j in range(m):
            if seats[i][j] >= 1:
                final_ans += 1

    print(final_ans)

solve2(grid)
