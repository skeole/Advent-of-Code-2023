import math
from copy import deepcopy
import time

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(C)

count = 0
power = 0
for i in range(len(X)):
    mult = 1
    n = X[i].split()
    t = [0, 0, 0]
    s = "rgb"
    n.pop(0)
    n.pop(0)
    for j in range(int(len(n) / 2)):
        if int(n[2 * j]) - s.index(n[2 * j + 1][0]) > 12:
            mult = 0
        t[s.index(n[2 * j + 1][0])] = max(int(n[2 * j]), t[s.index(n[2 * j + 1][0])])
    
    count += mult * (i + 1)
    power += t[0] * t[1] * t[2]

print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str(power))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))