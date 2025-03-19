import math
from copy import deepcopy
import time
from UsefulFunctions import *

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    C = C.split()
    C[1] = int(C[1])
    C.append("RDLU"[int(C[2][-2])])
    C[2] = C[2][2:-2]
    counter = 0
    for i in range(len(C[2])):
        counter += "0123456789abcdef".index(C[2][len(C[2]) - 1 - i]) * (16 ** i)
    C[2] = counter
    X.append(C)

# for part 1: shoelace theorem yay

coordinates = [[0, 0]]

for i in X:
    coordinates.append(two_d_vector_add(coordinates[-1], two_d_vector_multiply_scalar(two_d_vector_rotate_counterclockwise([0, 1], "RULD".index(i[0])), i[1])))

area = 0
for i in range(len(coordinates) - 1):
    area += 0.5 * (coordinates[i][0] * coordinates[i + 1][1] - coordinates[i][1] * coordinates[i + 1][0])
    
area = abs(area) + 1 # there are 4 unpaired + 0.75s, which leads to a deficit of 1

for i in X:
    area += 0.5 * (i[1]) # to account for edges only being half in

print("Part One Answer: " + str(round(area)))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

coordinates = [[0, 0]]

for i in X:
    coordinates.append(two_d_vector_add(coordinates[-1], two_d_vector_multiply_scalar(two_d_vector_rotate_counterclockwise([0, 1], "RULD".index(i[3])), i[2])))

area = 0
for i in range(len(coordinates) - 1):
    area += 0.5 * (coordinates[i][0] * coordinates[i + 1][1] - coordinates[i][1] * coordinates[i + 1][0])

area = abs(area) + 1 # there are 4 unpaired + 0.75s, which leads to a deficit of 1

for i in X:
    area += 0.5 * (i[2]) # to account for edges only being half in

print("Part Two Answer: " + str(round(area)))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))