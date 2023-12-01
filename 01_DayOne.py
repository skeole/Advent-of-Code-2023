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

for i in X:
    
    last = 0
    first = -1
    
    for j in range(len(i)):
        
        if i[j] in "0123456789":
            t = "0123456789".index(i[j])
            if first == -1:
                first = t
            last = t
            
    count += last + first * 10


print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

count = 0

for i in X:
    
    last = 0
    first = -1
    
    for j in range(len(i)):
        
        if i[j] in "0123456789":
            t = "0123456789".index(i[j])
            if first == -1:
                first = t
            last = t
        
        elif j + 2 < len(i) and ((i[j] + i[j + 1] + i[j + 2]) in ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]):
            t = ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"].index(i[j] + i[j + 1] + i[j + 2])
            if first == -1:
                first = t
            last = t
            
    count += last + first * 10

print("Part Two Answer: " + str(count))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))