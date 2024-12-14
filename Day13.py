from tqdm import tqdm
import numpy as np

input_file = open("input.txt", "r")
lines = input_file.readlines()
lines = [line.strip('\n') for line in lines]
lines = list(filter(lambda a: len(a) > 0, lines))

class Node:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v

def solve(arr):
    final_ans_sum = 0
    for i in range(0, len(arr), 3):
        # take values from this statemetn: Button A: X+{ax}, Y+{ay}
        ax = int(arr[i].split(' ')[2].split(',')[0][2:])
        ay = int(arr[i].split(' ')[3].split(',')[0][2:])

        # take values from this statemetn: Button B: X+{bx}, Y+{by}
        bx = int(arr[i + 1].split(' ')[2].split(',')[0][2:])
        by = int(arr[i + 1].split(' ')[3].split(',')[0][2:])

        # take values from this statement: Prize: X={kx}, Y={ky}
        kx = int(arr[i + 2].split(' ')[1].split(',')[0][2:])
        ky = int(arr[i + 2].split(' ')[2][2:])

        ans = [[Node(0, 0, float('inf')) for _ in range(101)] for _ in range(101)]
        ans[0][0] = Node(0, 0, 0)
        final_ans = float('inf')
        for x in range(100):
            for y in range(100):
                cur_n = ans[x][y]
                if cur_n.x == kx and cur_n.y == ky:
                    final_ans = min(final_ans, cur_n.v)
                ans[x + 1][y].x = cur_n.x + ax
                ans[x + 1][y].y = cur_n.y + ay
                ans[x + 1][y].v = cur_n.v + 3


                ans[x][y + 1].x = cur_n.x + bx
                ans[x][y + 1].y = cur_n.y + by
                ans[x][y + 1].v = cur_n.v + 1

        
        final_ans_sum += (final_ans if final_ans != float('inf') else 0)
    print(final_ans_sum)

def check(a, b, ax, ay, bx, by, kx, ky):
    a = round(a)
    b = round(b)

    return (kx - ax * a - bx * b) == 0 and (ky - ay * a - by * b) == 0


def solve2(arr):
    final_ans_sum = 0
    for i in range(0, len(arr), 3):
        # take values from this statemetn: Button A: X+{ax}, Y+{ay}
        ax = int(arr[i].split(' ')[2].split(',')[0][2:])
        ay = int(arr[i].split(' ')[3].split(',')[0][2:])

        # take values from this statemetn: Button B: X+{bx}, Y+{by}
        bx = int(arr[i + 1].split(' ')[2].split(',')[0][2:])
        by = int(arr[i + 1].split(' ')[3].split(',')[0][2:])

        # take values from this statement: Prize: X={kx}, Y={ky}
        kx = int(arr[i + 2].split(' ')[1].split(',')[0][2:]) + 10000000000000
        ky = int(arr[i + 2].split(' ')[2][2:]) + 10000000000000

        A = np.array([[ax, bx], [ay, by]])
        B = np.array([kx, ky])

        ans = np.linalg.solve(A, B)
        if check(ans[0], ans[1], ax, ay, bx, by, kx, ky):
            final_ans_sum += round(ans[0]) * 3 + round(ans[1])

    print(final_ans_sum)

solve2(lines)
