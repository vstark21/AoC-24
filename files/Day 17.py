with open('input.txt', 'r') as f:
    lines = f.readlines()
    iter_ = iter(lines)
    input = lambda: next(iter_)

global A, B, C
A = int(input().split()[-1])
B = int(input().split()[-1])
C = int(input().split()[-1])
_ = input()
arr = list(map(int, input().split()[-1].split(',')))

print(A, B, C, arr)

def get_combo(instr):
    return [0, 1, 2, 3, A, B, C, 7][instr]

def adv(idx):
    instr = arr[idx]
    global A
    A = A // (2 ** get_combo(instr))
    return idx + 1

def bxl(idx):
    instr = arr[idx]
    global B
    B = B ^ instr
    return idx + 1

def bst(idx):
    instr = arr[idx]
    global B
    B = get_combo(instr) % 8
    return idx + 1

def jnz(idx):
    instr = arr[idx]
    global A
    if A == 0:
        return idx + 1
    return instr

def bxc(idx):
    global B, C
    B = B ^ C
    return idx + 1

def out(idx):
    global FINAL_OUT
    FINAL_OUT.append(get_combo(arr[idx]) % 8)
    return idx + 1

def bdv(idx):
    instr = arr[idx]
    global A, B
    B = A // (2 ** get_combo(instr))
    return idx + 1

def cdv(idx):
    instr = arr[idx]
    global A, C
    C = A // (2 ** get_combo(instr))
    return idx + 1

opcode_func_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

def solve1(arr):
    idx = 0
    global FINAL_OUT
    FINAL_OUT = []
    while idx < len(arr):
        idx = opcode_func_map[arr[idx]](idx + 1)

    print(','.join(map(str, FINAL_OUT)))


def get_x(a, out):
    xs = []
    for x in range(0, 8):
        l1 = x ^ 4
        l2 = (a + x) // 2 ** l1
        l3 = l2 ^ l1
        left = l3 ^ 4
        left %= 8
        if left == out:
            xs.append(x)
    
    return xs


def rec(arr, idx, a):
    if idx == -1:
        print("DONE:", a)
        return
    a *= 8
    xs = get_x(a, arr[idx])
    if len(xs) == 0:
        return
    for x in xs:
        if idx == len(arr) - 1 and x == 0:
            continue
        rec(arr, idx - 1, a + x)


def solve2(arr):
    rec(arr, len(arr) - 1, 0)

solve1(arr)
print("PICK THE LEAST ONE: ")
solve2([2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0])