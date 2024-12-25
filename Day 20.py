from tqdm import tqdm
import numpy as np
import time
from queue import PriorityQueue
from collections import defaultdict

input_file = open("input.txt", "r")
lines = input_file.readlines()
grid = [list(line.strip()) for line in lines]

def get_neighbors(x, y):
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        yield nx, ny

def get_shortest_distance(
    start,
    end
):
    queue = PriorityQueue()
    queue.put((0, start))
    visited = set()
    visited.add(start)
    while not queue.empty():
        (cost, current) = queue.get()
        if current == end:
            return cost
        for nx, ny in get_neighbors(*current):
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.put((cost + 1, (nx, ny)))

    return -1

def cheat_shortest_distance(
    start,
    end,
    max_time,
    to_save
):
    class Node:
        def __init__(self, x, y, time, cheats):
            self.x = x
            self.y = y
            self.time = time
            self.cheats = cheats

        def __lt__(self, other):
            return self.time < other.time

    queue = PriorityQueue()
    queue.put(Node(start[0], start[1], 0, [0, (-1, -1), (-1, -1)]))
    visited = set()
    ans = 0
    from collections import defaultdict
    cheat_dic = defaultdict(int)
    cheat_vis = set()

    while not queue.empty():
        print(len(queue.queue))
        cur = queue.get()

        if cur.time > max_time:
            continue

        if (cur.x, cur.y, cur.cheats[1]) in visited:
            continue

        visited.add((cur.x, cur.y, cur.cheats[1]))

        if cur.x == end[0] and cur.y == end[1]:
            if (cur.cheats[1][0], cur.cheats[1][1], cur.cheats[2][0], cur.cheats[2][1]) not in cheat_vis:
                cheat_vis.add((cur.cheats[1][0], cur.cheats[1][1], cur.cheats[2][0], cur.cheats[2][1]))
                cheat_dic[max_time - cur.time] += 1

            continue

        for nx, ny in get_neighbors(cur.x, cur.y):
            if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                continue
            
            nex = Node(nx, ny, cur.time + 1, cur.cheats)
            if cur.cheats[0] == 0:
                if grid[nx][ny] == "#":
                    nex.cheats = [1, (nx, ny), (-1, -1)]
                queue.put(nex)
            elif cur.cheats[0] == 1:
                nex.cheats = [2, nex.cheats[1], (nx, ny)]
                if grid[nx][ny] == "#":
                    continue
                queue.put(nex)
            else:
                if grid[nx][ny] == "#":
                    continue
                queue.put(nex)
    
    ans = 0
    for el in cheat_dic.items():
        if el[0] >= to_save:
            ans += el[1]

        print(el[0], ":", el[1])

    return ans

def roam(
    start
):
    dist = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]

    queue = PriorityQueue()
    queue.put((0, start))
    dist[start[0]][start[1]] = 0
    
    while not queue.empty():
        d, (x, y) = queue.get()
        if d > dist[x][y]:
            continue
        for nx, ny in get_neighbors(x, y):
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] != "#" and dist[nx][ny] > d + 1:
                    dist[nx][ny] = d + 1
                    queue.put((d + 1, (nx, ny)))
                elif grid[nx][ny] == "#":
                    dist[nx][ny] = min(dist[nx][ny], d + 1)

    return dist

def cheat(
    start,
    end,
    least_time,
    to_save
):

    dist_s = roam(start)
    dist_e = roam(end)

    cheat_dic = defaultdict(int)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#" and dist_s[i][j] != float('inf') and dist_e[i][j] != float('inf'):
                print(i, j, dist_s[i][j], dist_e[i][j])
                cheat_dic[least_time - dist_s[i][j] - dist_e[i][j]] += 1

    ans = 0
    for el in cheat_dic.items():
        if el[0] >= to_save:
            ans += el[1]

    print(ans)

    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print(dist_s[i][j], end=" ")

    #     print()

def solve1():
    start = None
    end = None
    N = len(grid)
    M = len(grid[0])
    TO_SAVE = 100

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)


    least_time = get_shortest_distance(start, end)

    print(least_time)
    import time
    start_time = time.time()
    # ans = cheat_shortest_distance(start, end, least_time, TO_SAVE)

    cheat(start, end, least_time, TO_SAVE)

    print("--- %s seconds ---" % round(time.time() - start_time, 3))

# def solve2():

#     start = None
#     end = None
#     N = len(grid)
#     M = len(grid[0])

#     for i in range(N):
#         for j in range(M):
#             if grid[i][j] == "S":
#                 start = (i, j)
#             elif grid[i][j] == "E":
#                 end = (i, j)

#     least_time = get_shortest_distance(start, end)
    
#     class State:
#         def __init__(self, x, y, time, is_ch, cheat_len, cheat_start):
#             self.x = x
#             self.y = y
#             self.time = time
#             self.is_ch = is_ch
#             self.cheat_len = cheat_len
#             self.cheat_start = cheat_start

#         def __lt__(self, other):
#             return self.time < other.time

#     queue = PriorityQueue()
#     queue.put(State(start[0], start[1], 0, False, 0, (-1, -1)))
#     dist_s = [[float('inf')] * M for _ in range(N)]
#     count_s = [[0] * M for _ in range(N)]

#     while not queue.empty():
#         cur = queue.get()
#         if cur.time > dist_s[cur.x][cur.y]:
#             continue
#         dist_s[cur.x][cur.y] = cur.time
#         for nx, ny in get_neighbors(cur.x, cur.y):
#             if 0 <= nx < N and 0 <= ny < M:
                
#                 if grid[cur.x][cur.y] != '#':
#                     if grid[nx][ny] != '#':
#                         queue.put(State(nx, ny, cur.time + 1, False, cur.cheat_len, cur.cheat_start))
#                     else:
#                         if cur.cheat_len == 0:
#                             queue.put(State(nx, ny, cur.time + 1, True, 1, (nx, ny)))

#                 else:
#                     # if grid[nx][ny] != '#':
#                     #     queue.put(State(nx, ny, cur.time + 1, False, cur.cheat_len, cur.cheat_start))
#                     if grid[nx][ny] == '#':
#                         if cur.cheat_len < 19:
#                             queue.put(State(nx, ny, cur.time + 1, True, cur.cheat_len + 1, cur.cheat_start))


#     dist_e = roam(end)
    
#     cheat_dic = defaultdict(int)

#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == "#" and dist_s[i][j] != float('inf') and dist_e[i][j] != float('inf'):
#                 # print(i, j, dist_s[i][j], dist_e[i][j])
#                 cheat_dic[least_time - dist_s[i][j] - dist_e[i][j]] += 1

#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             print(f"{dist_s[i][j]:03}", end=" ")

#         print()

#     ans = 0
#     for el in cheat_dic.items():
#         if el[0] >= 50:
#             # print(el[0], ":", el[1])
#             ans += el[1]

#     print(ans)

def solve2():
    start = None
    end = None
    N = len(grid)
    M = len(grid[0])
    TO_SAVE = 100

    for i in range(N):
        for j in range(M):
            if grid[i][j] == "S":
                start = (i, j)
            elif grid[i][j] == "E":
                end = (i, j)


    least_time = get_shortest_distance(start, end)

    print(least_time)
    import time
    start_time = time.time()

    dist_s = roam(start)
    dist_e = roam(end)

    cheat_dic = defaultdict(int)
    
    for i in tqdm(range(N)):
        for j in range(M):
            if grid[i][j] == '#' or dist_s[i][j] == float('inf'):
                continue

            queue = PriorityQueue()
            for nx, ny in get_neighbors(i, j):
                if 0 <= nx < N and 0 <= ny < M:
                    queue.put((1, nx, ny))
            visited = set()
            reachable = set()

            while not queue.empty():
                d, x, y = queue.get()
                if d > 20:
                    continue
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                if grid[x][y] != '#':
                    reachable.add((x, y, d))

                for nx, ny in get_neighbors(x, y):
                    if 0 <= nx < N and 0 <= ny < M:
                        queue.put((d + 1, nx, ny))
                    
            for nx, ny, d in reachable:
                if dist_e[nx][ny] != float('inf'):
                    diff = least_time - dist_s[i][j] - dist_e[nx][ny] - d
                    if diff >= TO_SAVE:
                        cheat_dic[diff] += 1

    print(sum(cheat_dic.values()))
    print("--- %s seconds ---" % round(time.time() - start_time, 3))

# solve1()
solve2()

