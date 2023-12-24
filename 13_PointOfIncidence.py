import math
from copy import deepcopy
import time
import UsefulFunctions

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

temp = []
for line in file:
    C = line.strip()
    if C == "":
        X.append(temp)
        temp = []
    else:
        temp.append(list(C))

if temp != []:
    X.append(temp)
    temp = []

def test_symmetry(graph, target_failures=0):
    for i in range(0, len(graph[0]) - 1): # because obviously the two ends are going to work lmao
        failures = 0
        for j in range(len(graph)):
            for k in range(len(graph[0])): # if testing 0 -> 0 maps to 1; if 1 -> 1 maps to 2 -> 
                new_row = 2 * i + 1 - k
                if -1 < new_row and new_row < len(graph[0]):
                    if graph[j][k] != graph[j][new_row]:
                        failures += 1
        if failures == 2 * target_failures:
            return i + 1
    
    for i in range(0, len(graph) - 1): # same reasoning
        failures = 0
        for j in range(len(graph[0])):
            for k in range(len(graph)): # if testing 0 -> 0 maps to 1; if 1 -> 1 maps to 2 -> 
                new_col = 2 * i + 1 - k
                if -1 < new_col and new_col < len(graph):
                    if graph[k][j] != graph[new_col][j]:
                        failures += 1
        if failures == 2 * target_failures:
            return 100 * (i + 1)

count = 0
for i in X:
    count += test_symmetry(i)

print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

count = 0
for i in X:
    count += test_symmetry(i, target_failures=1)

print("Part Two Answer: " + str(count))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))