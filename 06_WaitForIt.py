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
    C.pop(0)
    for i in range(len(C)):
        C[i] = int(C[i])
    X.append(C)

prod = 1
for i in range(len(X[0])):
    t = X[0][i]
    d = X[1][i] + 0.01
    # distance: x * (t - x) >= d -> x^2 - tx + d <= 0 -> t ± sqrt(t^2 - 4d) / 2
    prod *= (math.floor((t + math.sqrt(t * t - 4 * d)) / 2) - math.ceil((t - math.sqrt(t * t - 4 * d)) / 2) + 1)

print("Part One Answer: " + str(prod))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

fs = ""
ss = ""
for i in range(len(X[0])):
    fs += str(X[0][i])
    ss += str(X[1][i])

fs = int(fs)
ss = int(ss) + 0.01

print("Part Two Answer: " + str(math.floor((fs + math.sqrt(fs * fs - 4 * ss)) / 2) - math.ceil((fs - math.sqrt(fs * fs - 4 * ss)) / 2) + 1))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))