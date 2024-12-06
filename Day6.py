from tqdm import tqdm

input_file = open("input.txt", "r")
lines = input_file.readlines()
lines = [list(lines[i].strip('\n')) for i in range(len(lines))]

def loop_detection(i, j, di, dj, arr):
    vis = set()
    si, sj = i + di, j + dj
    while 1:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= len(arr) or nj < 0 or nj >= len(arr[0]):
            return False
        
        if arr[ni][nj] == '#':
            di, dj = dj, di
            dj *= -1
            continue
        
        if (i, j, di, dj) in vis:
            return True
        vis.add((i, j, di, dj))
        
        i += di
        j += dj
        

def solve(arr):
    si, sj = 0, 0
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '^':
                si, sj = i, j

    di, dj = -1, 0
    ans = set()
    checked = set()
    ans1 = set()
    ans1.add((si, sj))
    while 1:
        ni, nj = si + di, sj + dj
        if ni < 0 or ni >= n or nj < 0 or nj >= m:
            break

        if arr[ni][nj] == '#':
            di, dj = dj, di
            dj *= -1
            continue
        elif arr[ni][nj] == '.' and (ni, nj) not in checked:
            arr[ni][nj] = '#'
            checked.add((ni, nj))
            if loop_detection(si, sj, di, dj, arr):
                ans.add((ni,nj))
            arr[ni][nj] = '.'
        si += di
        sj += dj
        ans1.add((si, sj))
    
    print("Part 1: ", len(ans1))
    print("Part 2: ", len(ans))

    ans1.add((si, sj))

solve(lines)
