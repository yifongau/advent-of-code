import os

input = "01-input.txt"

cola = []
colb = []
sim_score = 0

with open(input) as f:
    content = f.read().splitlines()

for line in content:
    split = line.split("   ")
    a = int(split[0])
    cola.append(a)

    b = int(split[1])
    colb.append(b)

seta = set(cola)

for val in seta:
    sim_score += val * colb.count(val)

print(sim_score)


    

