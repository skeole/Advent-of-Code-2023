import math
from copy import deepcopy
import time
import UsefulFunctions

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

S_Location = [0, 0] # row number, column number
for line in file:
    C = line.strip()
    C = list(C)
    if "S" in C:
        S_Location = [len(X), C.index("S")]
    X.append(C)

S_Value = ""
direction = 0 # 0 = right, 1 = up, 2 = left, 3 = down
if X[S_Location[0]][S_Location[1] + 1] in "J-7":
    if X[S_Location[0] + 1][S_Location[1]] in "J|L":
        S_Value = "F"
    elif X[S_Location[0] - 1][S_Location[1]] in "F|7":
        S_Value = "L"
    else:
        S_Value = "-"
    direction = 0
elif X[S_Location[0]][S_Location[1] - 1] in "F-L":
    if X[S_Location[0] - 1][S_Location[1]] in "F|7":
        S_Value = "J"
    elif X[S_Location[0] + 1][S_Location[1]] in "J|L":
        S_Value = "7"
    else:
        S_Value = "-"
    direction = 0
else:
    S_Value = "|"
    direction = 1

loop_values = [[S_Location[0], S_Location[1]]]
current_value = [S_Location[0], S_Location[1]]
if direction == 1:
    current_value[0] -= 1
else:
    current_value[1] += 1

while current_value != S_Location: # direction: 0 = right, 1 = up, 2 = left, 3 = down
    loop_values.append([current_value[0], current_value[1]])
    if X[current_value[0]][current_value[1]] == "-" or X[current_value[0]][current_value[1]] == "|":
        direction = direction
    elif X[current_value[0]][current_value[1]] == "F" or X[current_value[0]][current_value[1]] == "J": # 5 - x
        direction = (5 - direction) % 4
    else: # 3 - x:
        direction = 3 - direction
    
    if direction == 0:
        current_value[1] += 1
    elif direction == 1:
        current_value[0] -= 1
    elif direction == 2:
        current_value[1] -= 1
    elif direction == 3:
        current_value[0] += 1

new_x = ["."] * len(X)
for i in range(len(X)):
    new_x[i] = ["."] * len(X[0])

for i in loop_values:
    new_x[i[0]][i[1]] = X[i[0]][i[1]]

X = deepcopy(new_x)

X[S_Location[0]][S_Location[1]] = S_Value

print("Part One Answer: " + str(int(len(loop_values) / 2)))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

area = 0
for i in range(len(X)):
    count = 0
    for j in range(len(X[i])):
        if X[i][j] == "|":
            count += 2
        elif X[i][j] == "L" or X[i][j] == "7":
            count += 1
        elif X[i][j] == "J" or X[i][j] == "F":
            count += 3
        if X[i][j] != ".":
            continue
        elif count % 4 == 2:
            area += 1
                
print("Part Two Answer: " + str(area))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))