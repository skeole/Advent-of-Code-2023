import math
import random
from copy import deepcopy
import time
from UsefulFunctions import *
from queue import Queue

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

names = []
for line in file:
    C = line.strip().split(": ")
    names.append(C[0])
    X.append(C[1].split(" "))

counter = 0
for i in range(len(X)):
    for j in range(len(X[i])):
        if X[i][j] not in names:
            names.append(X[i][j])
            counter += 1
        X[i][j] = names.index(X[i][j])

for i in range(counter):
    X.append([])

for i in range(len(X)):
    for j in X[i]:
        if i not in X[j]:
            X[j].append(i) # or else we get double counting :)

for i in range(len(X)):
    X[i].sort()

edges = []
Y = []
for i in range(len(X)):
    Y.append([])
    for j in range(len(X[i])):
        if X[i][j] < i:
            Y[i].append(Y[X[i][j]][X[X[i][j]].index(i)])
        else:
            Y[i].append(len(edges))
            edges.append(0)

# another idea: random design :sob: do maximal paths idfk I WOULD LIKE TO LET IT BE KNOWN THIS WAS MY OG IDEA BEFORE LOOKING ON REDDIT FOR HINTS

number_of_visits = [0] * len(X)
for i in range(100):
    source = int(random.random() * len(X))
    target = int(random.random() * len(X))

    # now we want to find the shortest path from source to target
    
    distances = [99999] * len(X)
    distances[target] = 0
    queue = [target]

    while len(queue) > 0:
        lv = queue.pop(0)
        for j in X[lv]:
            if distances[j] > distances[lv] + 1:
                queue.append(j)
                distances[j] = distances[lv] + 1 # note: the furthest vertices are not necessarily in disjoint subsets usadgemoely
                # okay this isn't too bad...
    
    cd = distances[source]
    cv = source

    path = []
    while cd > 0:
        path.append(cv)
        nv = -1
        for j in X[cv]:
            if distances[j] < distances[cv]:
                nv = j
        cd -= 1
        edges[Y[cv][X[cv].index(nv)]] += 1
        cv = nv
    cd -= 1
    path.append(target)

M = deepcopy(edges)
M.sort()
largests = []
for i in range(3):
    largests.append(edges.index(M[-1 - i]))

cut_edges = []

for i in range(len(Y)):
    for j in range(len(Y[i])):
        if Y[i][j] in largests and i < X[i][j]:
            print("Cut edge: " + str(names[i]) + " to " + str(names[X[i][j]]))
            cut_edges.append([i, X[i][j]])
            cut_edges.append([X[i][j], i])

for i in cut_edges:
    X[i[0]].pop(X[i[0]].index(i[1]))


distances = [99999] * len(X)
distances[0] = 0
queue = [0]

while len(queue) > 0:
    lv = queue.pop(0)
    for j in X[lv]:
        if distances[j] > distances[lv] + 1:
            queue.append(j)
            distances[j] = distances[lv] + 1 # note: the furthest vertices are not necessarily in disjoint subsets usadgemoely
            # okay this isn't too bad...

c = 0
d = 0
for i in distances:
    if i == 99999:
        d += 1
    else:
        c += 1
# stupid fucking solution but idgaf

print("Part One Answer: " + str(c * d))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str("Merry Christmas :)"))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))