import math
from copy import deepcopy
import time
import UsefulFunctions

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split()
    C[0] = C[0].split(".")
    for i in range(len(C[0]) - 1, -1, -1):
        if len(C[0][i]) == 0:
            C[0].pop(i)
    C[1] = C[1].split(",")
    for i in range(len(C[1])):
        C[1][i] = int(C[1][i])
    X.append(C)

# bottleneck: ??????#???????????? 1,1,1,5,1,1
# as far as I can tell at least

def solve(hotspring, code):
    return 0

print("Part One Answer: " + str("part one answer"))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str("part two answer"))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))