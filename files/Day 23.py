from tqdm import tqdm
import numpy as np
import time
from queue import PriorityQueue
from collections import defaultdict

input_file = open("input.txt", "r")
lines = input_file.readlines()
edges = defaultdict(list)

for line in lines:
    a, b = line.strip('\n').split('-')
    edges[a].append(b)
    edges[b].append(a)

def solve1():
    triplets = set()
    nodes = list(edges.keys())

    for node in nodes:
        for neighbor in edges[node]:
            for neighbor2 in edges[neighbor]:
                if neighbor2 != node and neighbor2 in edges[node]:
                    triplet = tuple(sorted([node, neighbor, neighbor2]))
                    triplets.add(triplet)
    
    final_ans = 0
    for el in triplets:
        ans = False
        for node in el:
            if node[0] == 't':
                ans = True

        final_ans += int(ans)

    print(final_ans)


def solve2():
    nodes = list(edges.keys())

    for node in nodes:
        edges[node] = set(edges[node])

    def rec(node, cur_set, edges, vis, cur_ans):
        if len(cur_set) == 0:
            return cur_ans
        if vis[node]:
            return cur_ans
        
        vis[node] = True
        cur_ans += 1
        ans = cur_ans
        for el in cur_set:
            nex_set = cur_set.intersection(edges[el])
            ans = max(ans, rec(el, nex_set, edges, vis, cur_ans))

        return ans

    ans = 0
    ans_nodes = []
    for node in nodes:
        cur_ans = rec(node, edges[node].copy(), edges, defaultdict(lambda: False), 1)
    
        ans = max(ans, cur_ans)

        if cur_ans == 13:
            ans_nodes.append(node)

    ans_nodes.sort()
    print(",".join(ans_nodes))


solve1()
solve2()
