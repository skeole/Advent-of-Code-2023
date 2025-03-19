import math
from copy import deepcopy
import time
from UsefulFunctions import *
from queue import Queue

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(list(C))

X[0][1] = "#"
X[-1][-2] = "#"

Y = deepcopy(X)

# node structure: [index, distance] list

all_nodes = [[], []] # first is the entry, last is the exit
node_positions = [[0, 1], [len(X) - 1, len(X[0]) - 2]]

X = deepcopy(Y)

for i in range(1, len(X) - 1):
    for j in range(1, len(X[0]) - 1):

        if X[i][j] != "#":

            counter = 0
            if X[i][j + 1] != "#":
                counter += 1
            if X[i + 1][j] != "#":
                counter += 1
            if X[i][j - 1] != "#":
                counter += 1
            if X[i - 1][j] != "#":
                counter += 1

            if counter > 2:
                all_nodes.append([])
                node_positions.append([i, j])

for i in range(1, len(all_nodes)):
    X = deepcopy(Y)

    position = node_positions[i]
    u = []

    if i == 1:
        i = 0
        position = [0, 1]
        u.append([1, 1])
    else:
        if X[position[0]][position[1] + 1] == ">" or X[position[0]][position[1] + 1] == ".":
            u.append([position[0], position[1] + 1])
        if X[position[0] + 1][position[1]] == "v" or X[position[0] + 1][position[1]] == ".":
            u.append([position[0] + 1, position[1]])
        if X[position[0]][position[1] - 1] == "<" or X[position[0]][position[1] - 1] == ".":
            u.append([position[0], position[1] - 1])
        if X[position[0] - 1][position[1]] == "^" or X[position[0] - 1][position[1]] == ".":
            u.append([position[0] - 1, position[1]])
    
    for sp in u:
        X = deepcopy(Y)
        
        X[0][1] = "."
        X[-1][-2] = "."

        X[position[0]][position[1]] = "#"

        length = 0

        while True:
            X[sp[0]][sp[1]] = "O"
            length += 1
            if sp[0] == 0 and sp[1] == 1:
                all_nodes[i].append([0, length])
                break
            if sp[0] == len(X) - 2 and sp[1] == len(X[0]) - 2:
                all_nodes[i].append([1, length])
                break
            counter = 0
            if X[sp[0]][sp[1] + 1] == ">" or X[sp[0]][sp[1] + 1] == ".":
                counter += 1
            if X[sp[0] + 1][sp[1]] == "v" or X[sp[0] + 1][sp[1]] == ".":
                counter += 1
            if X[sp[0]][sp[1] - 1] == "<" or X[sp[0]][sp[1] - 1] == ".":
                counter += 1
            if X[sp[0] - 1][sp[1]] == "^" or X[sp[0] - 1][sp[1]] == ".":
                counter += 1
            
            if counter != 1:
                all_nodes[i].append([node_positions.index(sp), length])
                break
            else:
                if X[sp[0]][sp[1] + 1] == ">" or X[sp[0]][sp[1] + 1] == ".":
                    sp[1] += 1
                elif X[sp[0] + 1][sp[1]] == "v" or X[sp[0] + 1][sp[1]] == ".":
                    sp[0] += 1
                elif X[sp[0]][sp[1] - 1] == "<" or X[sp[0]][sp[1] - 1] == ".":
                    sp[1] -= 1
                elif X[sp[0] - 1][sp[1]] == ">" or X[sp[0] - 1][sp[1]] == ".":
                    sp[0] -= 1

# total length of a path: sum of all lengths, plus one

q = Queue() # each entry is a structure: [current_node, current_length]
q.put([0, 1])

maxlength = 0

while q.qsize() > 0:
    current_node, current_length = q.get()

    if current_node == 1:
        maxlength = max(maxlength, current_length)
        continue

    for i in all_nodes[current_node]:
        q.put([i[0], current_length + i[1]]) # for some reason, keeping pv in doesn't increase run time much - setup is the majority here lol

print("Part One Answer: " + str(maxlength))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))

start = time.time()
print()

all_nodes = [[], []]
node_positions = [[0, 1], [len(X) - 1, len(X[0]) - 2]]

X = deepcopy(Y)

for i in range(1, len(X) - 1):
    for j in range(1, len(X[0]) - 1):

        if X[i][j] != "#":

            counter = 0
            if X[i][j + 1] != "#":
                counter += 1
            if X[i + 1][j] != "#":
                counter += 1
            if X[i][j - 1] != "#":
                counter += 1
            if X[i - 1][j] != "#":
                counter += 1
            
            if counter > 2:
                all_nodes.append([])
                node_positions.append([i, j])

for i in range(2, len(all_nodes)):
    X = deepcopy(Y)

    position = node_positions[i]
    u = []

    if X[position[0]][position[1] + 1] != "#":
        u.append([position[0], position[1] + 1])
    if X[position[0] + 1][position[1]] != "#":
        u.append([position[0] + 1, position[1]])
    if X[position[0]][position[1] - 1] != "#":
        u.append([position[0], position[1] - 1])
    if X[position[0] - 1][position[1]] != "#":
        u.append([position[0] - 1, position[1]])
    
    for sp in u:
        X = deepcopy(Y)
        
        X[0][1] = "."
        X[-1][-2] = "."

        X[position[0]][position[1]] = "#"

        length = 0

        while True:
            X[sp[0]][sp[1]] = "#"
            length += 1
            if sp[0] == 0 and sp[1] == 1:
                all_nodes[i].append([0, length])
                all_nodes[0].append([i, length])
                break
            if sp[0] == len(X) - 2 and sp[1] == len(X[0]) - 2:
                all_nodes[i].append([1, length])
                all_nodes[1].append([i, length])
                break
            counter = 0
            if X[sp[0]][sp[1] + 1] != "#":
                counter += 1
            if X[sp[0] + 1][sp[1]] != "#":
                counter += 1
            if X[sp[0]][sp[1] - 1] != "#":
                counter += 1
            if X[sp[0] - 1][sp[1]] != "#":
                counter += 1
            
            if counter != 1:
                all_nodes[i].append([node_positions.index(sp), length])
                break
            else:
                if X[sp[0]][sp[1] + 1] != "#":
                    sp[1] += 1
                elif X[sp[0] + 1][sp[1]] != "#":
                    sp[0] += 1
                elif X[sp[0]][sp[1] - 1] != "#":
                    sp[1] -= 1
                elif X[sp[0] - 1][sp[1]] != "#":
                    sp[0] -= 1

all_nodes[all_nodes[1][0][0]] = [[1, all_nodes[1][0][1]]]

distances_from_zero = [-1] * len(all_nodes)

q = Queue()
q.put([0, 0])

while q.qsize() > 0:
    node, distance = q.get()
    distances_from_zero[node] = distance
    for i in all_nodes[node]:
        if distances_from_zero[i[0]] == -1:
            q.put([i[0], distance + 1])

hi = []
for i in range(len(all_nodes)):
    for j in range(len(all_nodes)):
        if len(all_nodes[i]) < 4 and len(all_nodes[j]) < 4:
            if distances_from_zero[i] > distances_from_zero[j]:
                hi.append([i, j])

for i in range(len(all_nodes)):
    for j in range(len(all_nodes[i]) - 1, -1, -1):
        if [i, all_nodes[i][j][0]] in hi:
            all_nodes[i].pop(j)

q = Queue() # each entry is a structure: [previous_visits, current_node, current_length]
q.put([[], 0, 1])

maxlength = 0

count = 0

percent = 0

while q.qsize() > 0:
    previous_visits, current_node, current_length = q.get()

    if current_node == 1:
        count += 1
        pct = count / 1262816 * 100
        if pct > percent:
            percent += 10
            print(str(percent) + " percent done")
        maxlength = max(maxlength, current_length)
        continue

    for i in all_nodes[current_node]:
        pv = previous_visits.copy()
        pv.append(current_node)

        if i[0] not in previous_visits:
            q.put([pv, i[0], current_length + i[1]])

print("Part Two Answer: " + str(maxlength)) # roughly 18 seconds; without reddit help it took 108 seconds. Not bad!
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))