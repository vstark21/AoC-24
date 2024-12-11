from tqdm import tqdm

input_file = open("test_input.txt", "r")
lines = input_file.readlines()
lines = list(map(int, lines[0].split()))

def solve(arr):
    n_steps = 25
    for step in range(n_steps):
        new_arr = []
        for el in arr:
            sel = str(el)
            if el == 0:
                new_arr.append(1)
            elif len(sel) % 2 == 0:
                new_arr.append(int(sel[:len(sel) // 2]))
                new_arr.append(int(sel[len(sel) // 2:]))
            else:
                new_arr.append(el * 2024)

        arr = new_arr
    
    for step in tqdm(range(n_steps)):
        new_arr = []
        for el in arr:
            sel = str(el)
            if el == 0:
                new_arr.append(1)
            elif len(sel) % 2 == 0:
                new_arr.append(int(sel[:len(sel) // 2]))
                new_arr.append(int(sel[len(sel) // 2:]))
            else:
                new_arr.append(el * 2024)

        arr = new_arr

    print(len(new_arr))
solve(lines)