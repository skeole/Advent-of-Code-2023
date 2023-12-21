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
    firsts = []
    seconds = []
    for i in range(2, C.index("|")):
        firsts.append(int(C[i]))
    for i in range(C.index("|") + 1, len(C)):
        seconds.append(int(C[i]))
    X.append([deepcopy(firsts), deepcopy(seconds)])

scores = []
for i in X:
    t = 0.5
    for j in i[1]:
        if j in i[0]:
            t *= 2
    scores.append(int(t))

print("Part One Answer: " + str(sum(scores)))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

for i in range(len(scores)):
    if scores[i] == 0:
        scores[i] = 0
    else:
        scores[i] = round(math.log(scores[i]) / math.log(2)) + 1

cards = [-1] * len(scores)

def solve(index):
    if cards[index] != -1:
        return cards[index]
    else:
        scr = 1
        for i in range(index + 1, index + 1 + scores[index]):
            if i < len(scores):
                scr += solve(i)
        cards[index] = scr
        return scr

for i in range(len(scores)):
    solve(i)

print("Part Two Answer: " + str(sum(cards)))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))