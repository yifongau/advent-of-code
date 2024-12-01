import os

input = "01-input.txt"

cola = []
colb = []
colc = []

def diff(a,b):
    if a > b:
        return a-b
    elif b > a:
        return b-a
    else:
        return 0

with open(input) as f:
    content = f.read().splitlines()

for line in content:
    split = line.split("   ")
    a = int(split[0])
    cola.append(a)

    b = int(split[1])
    colb.append(b)

for i in range((len(content))):
    colc.append(diff(sorted(cola)[i],sorted(colb)[i]))

print(sum(colc))
    

