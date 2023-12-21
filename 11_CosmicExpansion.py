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
    X.append(list(C))

expanded_rows = []
expanded_cols = []
for i in range(len(X)):
    if X[i] == ["."] * len(X[i]):
        expanded_rows.append(i)

for i in range(len(X[0])):
    t = True
    for j in range(len(X)):
        t = t and X[j][i] == "."
    if t:
        expanded_cols.append(i)

galaxies = []

for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] == "#":
            galaxies.append([i, j])

rows = [0] * len(galaxies)
cols = [0] * len(galaxies)

for i in range(len(galaxies)):
    rows[i] = galaxies[i][1]
    cols[i] = galaxies[i][0]

rows.sort()
cols.sort()

init_space = 0 # if length is 4 -> -3, -1, 1, 3; if length is 5 -> -4, -2, 0, 2, 4
for i in range(len(rows)):
    init_space += (1 - len(galaxies) + 2 * i) * rows[i] + (1 - len(galaxies) + 2 * i) * cols[i]

for i in range(len(galaxies)):
    row_add = 0
    col_add = 0
    for j in expanded_rows:
        if j < galaxies[i][0]:
            row_add += 1
    for j in expanded_cols:
        if j < galaxies[i][1]:
            col_add += 1
    galaxies[i] = [galaxies[i][0] + row_add, galaxies[i][1] + col_add]

rows = [0] * len(galaxies)
cols = [0] * len(galaxies)

for i in range(len(galaxies)):
    rows[i] = galaxies[i][1]
    cols[i] = galaxies[i][0]

rows.sort()
cols.sort()

space = 0 # if length is 4 -> -3, -1, 1, 3; if length is 5 -> -4, -2, 0, 2, 4
for i in range(len(rows)):
    space += (1 - len(galaxies) + 2 * i) * rows[i] + (1 - len(galaxies) + 2 * i) * cols[i]

diff = space - init_space

print("Part One Answer: " + str(space))
print("Part One Runtime : " + str(int((time.time() - start) * 1000 + 0.5) / 1000))
start = time.time()
print()

print("Part Two Answer: " + str(init_space + diff * (1000000 - 1)))
print("Part Two Runtime : " + str(int((time.time() - start) * 1000 + 0.5) / 1000))