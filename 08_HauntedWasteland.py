import math
from copy import deepcopy
import time
import UsefulFunctions

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

left_right = []
instructions = [0] * (26 ** 3)

def character_to_index(character):
    s = 0
    for i in range(len(character)):
        s += 26 ** (2 - i) * "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(character[i])
    return s

for line in file:
    C = line.strip()
    if len(C) != 16:
        for letter in C:
            left_right.append("LR".index(letter))
    else:
        instructions[character_to_index(C[0 : 3])] = [character_to_index(C[7 : 10]), character_to_index(C[12 : 15])]

index = 0
count = 0
while index != (26 ** 3) - 1:
    index = instructions[index][left_right[count % len(left_right)]]
    count += 1

print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

indices = []

for i in range(26 ** 2):
    if instructions[26 * i] != 0:
        indices.append(26 * i)

counts = []
for i in indices:
    count = 0
    index = i
    while index % 26 != 25 or count % len(left_right) != 0:
        index = instructions[index][left_right[count % len(left_right)]]
        count += 1
    counts.append(count)

t = 1
for i in counts:
    t = math.lcm(t, i)

print("Part Two Answer: " + str(t))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))