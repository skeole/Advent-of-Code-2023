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
pairs = []

for i in range(1, len(X) - 1):
    j = 1
    while (j < len(X[0])):
        if X[i][j] in "0123456789":
            temp = ""
            symbol = False
            fin = False
            index = 0
            index_shift = -1000 + i * 10000000 + j * 1000
            while X[i][j] in "0123456789":
                index_shift += 1000
                temp += X[i][j]
                array = [X[i - 1][j - 1], X[i - 1][j], X[i - 1][j + 1], X[i][j - 1], X[i][j + 1], X[i + 1][j - 1], X[i + 1][j], X[i + 1][j + 1]]
                for k in range(len(array)):
                    if array[k] not in "0123456789.":
                        symbol = True
                        index_shift += [-10000000-1000, -10000000, -10000000+1000, 
                                       -1000,                       1000, 
                                       10000000-1000, 10000000, 10000000+1000][k]
                        if array[k] == "*" and index == 0:
                            index = index_shift
                j += 1
            if (symbol):
                count += int(temp)
            if (index != 0):
                pairs.append([int(temp), index])
                index = 0
        else:
            j += 1
        
print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

def funkyfunction(arr):
    return arr[1]

pairs = UsefulFunctions.sortarraysonfunction(pairs, funkyfunction)[0]

sumprod = 0
for i in range(len(pairs) - 1):
    if pairs[i][1] == pairs[i + 1][1]:
        sumprod += pairs[i][0] * pairs[i + 1][0]

print("Part Two Answer: " + str(sumprod))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))