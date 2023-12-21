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
    for i in range(len(C)):
        C[i] = int(C[i])
    X.append(C)

def polynomial_interpolation(values, x_value):
    func = 0
    for i in range(len(values)):
        temp_prod = 1
        for j in range(len(values)):
            if i != j:
                temp_prod *= (x_value - j) / (i - j)
        func += temp_prod * values[i]
    return round(func) # round to avoid weird integer errors

s = 0
n = 0

for i in X:
    s += polynomial_interpolation(i, len(i))
    n += polynomial_interpolation(i, -1)

print("Part One Answer: " + str(s))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str(n))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))