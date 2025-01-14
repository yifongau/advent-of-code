import os

input = "02-input.txt"

def is_safe(line):

    if line[0] == line[1]:
        return 0

    elif line[0] > line[1]:
        for n in range(len(line)-1):
            if line[n] > line[n+1]:
                if 0 < line[n] - line[n+1] < 4:
                    continue
                else: return 0
            else: return 0
        return 1

    elif line[0] < line[1]:
        for n in range(len(line)-1):
            if line[n] < line[n+1]:
                if 0 < line[n+1] - line[n] < 4:
                    continue
                else: return 0
            else: return 0
        return 1
            
with open(input) as f:
    content = f.read().splitlines()

count = 0
for line in content:
    line_arr = []
    split = line.split()

    for string in split:
        i = int(string)
        line_arr.append(i)

    count += is_safe(line_arr)
    
print(count)



