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
    X = C.split(",")

def evaluate_hash(sequence):
    count = 0
    for letter in sequence:
        count = ((count + UsefulFunctions.to_ascii(letter)) * 17) % 256
    return count

count = 0
for i in X:
    count += evaluate_hash(i)

print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

lenses = [] # each lens here contains the value
values = []
orders = []

boxes = [0] * 256 # contains the lenses in order

for i in range(len(boxes)):
    boxes[i] = []

for i in range(len(X)):
    X[i] = X[i].split("=")
    if len(X[i]) == 1:
        X[i].append(0)
        X[i][0] = X[i][0][:-1]
    else:
        X[i][1] = int(X[i][1])
    number = evaluate_hash(X[i][0])
    
    if X[i][0] not in lenses:
        lenses.append(X[i][0])
        values.append(0)
        orders.append(0)
        boxes[number].append(X[i][0])
    
    ind = lenses.index(X[i][0])
    if X[i][1] == 0: # remove
        if values[ind] != 0:
            for j in boxes[number]:
                if orders[lenses.index(j)] > orders[ind]:
                    orders[lenses.index(j)] -= 1
            orders[ind] = 0
            values[ind] = 0
    else:
        if values[ind] == 0:
            newind = 0
            for j in boxes[number]:
                newind = max(newind, orders[lenses.index(j)])
            orders[ind] = newind + 1
            values[ind] = X[i][1]
        else:
            values[ind] = X[i][1]

count = 0
for i in range(len(lenses)):
    count += orders[i] * values[i] * (evaluate_hash(lenses[i]) + 1)

print("Part Two Answer: " + str(count))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))