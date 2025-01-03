from tqdm import tqdm
import numpy as np
import time
from queue import PriorityQueue

input_file = open("input.txt", "r")
lines = input_file.readlines()
coords = [list(map(int, line.split(','))) for line in lines]

# N, M = 6 + 1, 6 + 1
# k = 12
N, M = 70 + 1, 70 + 1
k = 1024

grid = [['.' for _ in range(M)] for _ in range(N)]
for x, y in coords[:k]:
    grid[y][x] = '#'

start = (0, 0)
end = (N-1, M-1)

for i in range(N):
    for j in range(M):
        print(grid[i][j], end='')
    print()


def shortest_path(grid, start, end):
    pq = PriorityQueue()
    pq.put((0, start))
    visited = set()
    while not pq.empty():
        dist, node = pq.get()
        if node == end:
            return dist
        if node in visited:
            continue
        visited.add(node)
        x, y = node
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == '.' and (nx, ny) not in visited:
                pq.put((dist + 1, (nx, ny)))
    return -1

def solve1():
    print(shortest_path(grid, start, end))

def solve2():
    for i in tqdm(range(k, len(coords))):
        x, y = coords[i]
        grid[y][x] = '#'

        if shortest_path(grid, start, end) == -1:
            print((x, y))
            break

solve2()
