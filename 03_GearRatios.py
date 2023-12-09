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
    C.insert(0, ".")
    C.append(".")
    X.append(C)

t = ["."] * len(X[0])
X.insert(0, deepcopy(t))
X.append(deepcopy(t))

count = 0
stars = []

for i in range(1, len(X) - 1):
    j = 1
    while (j < len(X[0])):
        if X[i][j] in "0123456789":
            temp = ""
            symbol = False
            while X[i][j] in "0123456789":
                temp += X[i][j]
                array = [X[i - 1][j - 1], X[i - 1][j], X[i - 1][j + 1], X[i][j - 1], X[i][j + 1], X[i + 1][j - 1], X[i + 1][j], X[i + 1][j + 1]]
                for k in array:
                    if k not in "0123456789.":
                        symbol = True
                j += 1
            if (symbol):
                count += int(temp)
        else:
            j += 1
        
print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str("part two answer"))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))