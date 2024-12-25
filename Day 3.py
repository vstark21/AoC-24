input_file = open("input.txt", "r")
lines = input_file.readlines()

def part1(line: str):
    i = 0
    n = len(line)
    ret = 0
    while i >= 0 and i < n:
        i = line.find("mul", i)
        if i == -1:break
        i += 3
        if i > n:break

        if line[i] != '(':continue
        i += 1

        a = 0
        while line[i].isdigit():
            a = a * 10 + int(line[i])
            i += 1
        
        if line[i] != ',':continue
        i += 1

        b = 0
        while line[i].isdigit():
            b = b * 10 + int(line[i])
            i += 1
        
        if line[i] != ')':continue
        i += 1

        ret += (a * b)

    return ret

def part2(line: str):
    n = len(line)
    ret = 0
    global k
    for i in range(n):
        if line[i] == 'd':
            if line[i:i+7] == "don't()":
                k = 0
            elif line[i:i+4] == "do()":
                k = 1
        elif line[i:i+3] == 'mul':
            pass
        else:
            continue

        i += 3
        if i > n:break

        if line[i] != '(':continue
        i += 1

        a = 0
        while line[i].isdigit():
            a = a * 10 + int(line[i])
            i += 1
        
        if line[i] != ',':continue
        i += 1

        b = 0
        while line[i].isdigit():
            b = b * 10 + int(line[i])
            i += 1
        
        if line[i] != ')':continue
        i += 1

        ret += k * (a * b)

    return ret

k = 1
ans = sum(part2(line) for line in lines)
print(ans)