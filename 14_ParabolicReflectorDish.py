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
    C = list(C)
    C.insert(0, "#")
    C.append("#")
    X.append(list(C))

X.insert(0, ["#"] * len(X[0]))
X.append(["#"] * len(X[0]))

cache = [deepcopy(X)]

def iter(iter_num): # 0 -> neg y; 1 -> neg x; 2 -> plus y; 3 -> plus x
    iter_num = iter_num % 4
    if iter_num == 0:
        for i in range(1, len(X)):
            for j in range(len(X[0])):
                if X[i][j] == "O" and X[i - 1][j] == ".":
                    c = i - 1
                    while X[c - 1][j] == ".":
                        c -= 1
                    X[i][j] = "."
                    X[c][j] = "O"
    elif iter_num == 1:
        for i in range(1, len(X[0])):
            for j in range(len(X)):
                if X[j][i] == "O" and X[j][i - 1] == ".":
                    c = i - 1
                    while X[j][c - 1] == ".":
                        c -= 1
                    X[j][i] = "."
                    X[j][c] = "O"
    elif iter_num == 2:
        for i in range(len(X) - 2, 0, -1):
            for j in range(len(X[0])):
                if X[i][j] == "O" and X[i + 1][j] == ".":
                    c = i + 1
                    while X[c + 1][j] == ".":
                        c += 1
                    X[i][j] = "."
                    X[c][j] = "O"
    elif iter_num == 3:
        for i in range(len(X[0]) - 2, 0, -1):
            for j in range(len(X)):
                if X[j][i] == "O" and X[j][i + 1] == ".":
                    c = i + 1
                    while X[j][c + 1] == ".":
                        c += 1
                    X[j][i] = "."
                    X[j][c] = "O"

def calculate_load(arrangement):
    load = 0
    for i in range(len(arrangement)):
        for j in arrangement[i]:
            if j == "O":
                load += len(arrangement) - i - 1
    return load

iter(0)

print("Part One Answer: " + str(calculate_load(X)))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

iter(1)
iter(2)
iter(3)

while X not in cache:
    cache.append(deepcopy(X))
    iter(0)
    iter(1)
    iter(2)
    iter(3)

print("Part Two Answer: " + str(calculate_load(cache[cache.index(X) + (1000000000 - cache.index(X)) % (len(cache) - cache.index(X))])))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))