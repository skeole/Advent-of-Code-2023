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
    C[0] = list(C[0])
    for i in range(len(C[0])):
        C[0][i] = "23456789TJQKA".index(C[0][i])
    C[1] = int(C[1])
    X.append(C)

def relative_strength(card): # card values
    return 28561 * card[0] + 2197 * card[1] + 169 * card[2] + 13 * card[3] + card[4]

def absolute_strength(card, jokers_enabled = False): # 371293 * level
    letters = []
    counts = []
    jokers = 0
    for i in card:
        if jokers_enabled and i == 0:
            jokers += 1
        elif i in letters:
            counts[letters.index(i)] += 1
        else:
            letters.append(i)
            counts.append(1)
    counts.sort()
    counts.reverse()
    
    if len(counts) == 0:
        counts.append(0)
    counts[0] += jokers
    
    if counts[0] == 5:
        return 371293 * 6
    elif counts[0] == 4:
        return 371293 * 5
    elif counts[0] == 3 and counts[1] == 2:
        return 371293 * 4
    elif counts[0] == 3:
        return 371293 * 3
    elif counts[0] == 2 and counts[1] == 2:
        return 371293 * 2
    elif counts[0] == 2:
        return 371293 * 1
    else:
        return 0

def score(card, jokers_enabled = False):
    return relative_strength(card) + absolute_strength(card, jokers_enabled = jokers_enabled)

scores = []
for i in X:
    scores.append([i[1], score(i[0])])

def funkyfunction(arr):
    return arr[1]

scores = UsefulFunctions.sortarraysonfunction(scores, funkyfunction)[0]

ovrscore = 0
for i in range(len(scores)):
    ovrscore += scores[i][0] * (i + 1)

print("Part One Answer: " + str(ovrscore))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

for i in range(len(X)):
    for j in range(len(X[i][0])):
        if X[i][0][j] < 9:
            X[i][0][j] += 1
        elif X[i][0][j] == 9:
            X[i][0][j] = 0

scores = []
for i in X:
    scores.append([i[1], score(i[0], jokers_enabled = True)])

scores = UsefulFunctions.sortarraysonfunction(scores, funkyfunction)[0]

ovrscore = 0
for i in range(len(scores)):
    ovrscore += scores[i][0] * (i + 1)

print("Part Two Answer: " + str(ovrscore))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))