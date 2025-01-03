from tqdm import tqdm
import numpy as np
from queue import PriorityQueue
from collections import defaultdict
from collections import deque

input_file = open("input.txt", "r")
lines = input_file.readlines()

class Node:
    def __init__(self, name=None, v=None, i1=None, i2=None, typ=None):
        self.name = name
        self.v = v
        self.i1 = i1
        self.i2 = i2
        self.typ = None
        self.nex = []

    def compute(self, dic):
        if self.typ is None:
            return
        v1 = dic[self.i1].v
        v2 = dic[self.i2].v

        if v1 is None or v2 is None:
            return
        
        if self.typ == "AND":
            self.v = v1 & v2
        elif self.typ == "OR":
            self.v = v1 | v2
        elif self.typ == "XOR":
            self.v = v1 ^ v2


dic = defaultdict(Node)
queue = []
while lines:
    line = lines.pop(0).strip()
    if line == "":
        break

    line = line.split(" ")
    dic[line[0][:-1]] = Node(name=line[0][:-1], v=int(line[1]))
    queue.append(line[0][:-1])

while lines:
    line = lines.pop(0).strip()
    if line == "":
        break

    line = line.split(" ")

    i1 = line[0]
    typ = line[1]
    i2 = line[2]

    out = line[4]

    dic[out].name = out
    dic[out].typ = typ
    dic[out].i1 = i1
    dic[out].i2 = i2
    dic[i1].nex.append(out)
    dic[i2].nex.append(out)


def solve1():
    while queue:
        name = queue.pop(0)
        dic[name].compute(dic)

        for el in dic[name].nex:
            queue.append(el)

    ans_dic = {}
    for k in dic.keys():
        if k.startswith("z"):
            ans_dic[k] = dic[k].v

    keys = list(ans_dic.keys())
    keys.sort(reverse=True)
    ans = ""
    for k in keys:
        ans += str(ans_dic[k])
    print(int(ans, 2))

def find_gate(a, b, typ):
    common = set(dic[a].nex).intersection(set(dic[b].nex))
    for el in common:
        if dic[el].typ == typ:
            return el
    return None
        

def build_addition_gate(a, b, cin):
    xor1 = find_gate(a, b, "XOR")
    and1 = find_gate(a, b, "AND")

    xor2 = find_gate(xor1, cin, "XOR")
    and2 = find_gate(xor1, cin, "AND")

    cout = find_gate(and1, and2, "OR")

    return xor1, and1, and2

def reverse_addition_gate(s):
    # full adder
    cin = dic[s].i1 if dic[dic[s].i1].typ == "OR" else dic[s].i2
    xor1 = dic[s].i1 if dic[dic[s].i1].typ == "XOR" else dic[s].i2

    return xor1, cin

def swap(a, b):
    temp = dic[a]
    dic[a] = dic[b]
    dic[b] = temp

    # temp = dic[a].name
    # dic[a].name = dic[b].name
    # dic[b].name = temp


def solve2():
    # addition with bits
    # x: [x00, x01, ... nbits], y: [000, 001, ... nbits]
    # x + y = z = [z00, z01, ... n + 1bits]
    n_bits = 45 # 6 or 45
    carry = None
    final_ans = []
    for i in range(n_bits):
        # AND
        x_name = "x" + f"{i:02}"
        y_name = "y" + f"{i:02}"
        z_name = "z" + f"{i:02}"
        
        if carry is None:
            cout = find_gate(x_name, y_name, "AND")
            out = find_gate(x_name, y_name, "XOR")
            carry = cout
            continue

        else:
            xor1, and1, and2 = build_addition_gate(x_name, y_name, carry)
            rxor1, xcin = reverse_addition_gate(z_name)

            cout = find_gate(and1, and2, "OR")
            out = find_gate(xor1, carry, "XOR")

            if rxor1 != xor1 or out != z_name:
                if z_name == "z15":
                    print(out, z_name)
                    final_ans.extend([out, z_name])
                    swap(out, z_name)
                elif z_name == "z21":
                    print(out, z_name)
                    final_ans.extend([out, z_name])
                    swap(out, z_name)
                    cout = "fsh"
                elif z_name == "z30":
                    print("jrs", "wrk")
                    final_ans.extend(["jrs", "wrk"])
                    swap("jrs", "wrk")
                    cout = "hpt"
                elif z_name == 'z34':
                    print(out, z_name)
                    final_ans.extend([out, z_name])
                    swap(out, z_name)
                    cout = "bjj"
                else:
                    print("AMBIGUITY DETECTED")
                    print('---', x_name, y_name, z_name, '---')
                    print(carry, xor1, out, cout)
                    print(rxor1, carry, z_name)

            carry = cout

    final_ans.sort()
    print(",".join(final_ans))

# solve1()
# lot of manual analysis of addition gate
solve2()
