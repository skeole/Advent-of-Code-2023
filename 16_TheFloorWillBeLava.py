import math
from copy import deepcopy
import time
import UsefulFunctions

start = time.time()
X = []
empty_grid = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip()
    X.append(list(C))
    empty_grid.append([1] * len(C))

treg = deepcopy(empty_grid)

# 0: 2
# 1: 3
# 2: 5
# 3: 7

primes = [2, 3, 5, 7]

def calculate(position=[0, 0], direction=0, reset=True): # 0 = Right, 1 = Down, 2 = Left, 3 = Up
    # | splits from even to 1 AND 3, or preserves odd
    # - splits from odd to 0 AND 2, or preserves even
    # \ means 1 - direction
    # / means 3 - direction
    
    # first = row number (y), second = column number (x)
    
    global empty_grid
    
    if reset:
        empty_grid = deepcopy(treg)
    
    pos = [position[0], position[1]]
    direct = direction
    current_character = ""
    
    while True:
        if pos[0] < 0 or pos[1] < 0 or pos[0] > len(X) - 1 or pos[1] > len(X[0]) - 1 or empty_grid[pos[0]][pos[1]] % primes[direct] == 0:
            break
        
        empty_grid[pos[0]][pos[1]] *= primes[direct]
        
        current_character = X[pos[0]][pos[1]]
        
        if current_character == "|" and direct % 2 == 0:
            calculate(position=pos, direction=1, reset=False)
            direct = 3
        if current_character == "-" and direct % 2 == 1:
            calculate(position=pos, direction=0, reset=False)
            direct = 2
        
        if current_character == "\\":
            direct = (5 - direct) % 4
        elif current_character == "/":
            direct = 3 - direct
        
        if direct == 0:
            pos[1] += 1
        elif direct == 1:
            pos[0] += 1
        elif direct == 2:
            pos[1] -= 1
        elif direct == 3:
            pos[0] -= 1
    
    count = 0
    for i in empty_grid:
        for j in i:
            if j != 1:
                count += 1
    
    return count
    
print("Part One Answer: " + str(calculate()))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

def smortprint():
    for i in empty_grid:
        string = ""
        for j in i:
            if j == 2:
                string += ">"
            elif j == 3:
                string += "v"
            elif j == 5:
                string += "<"
            elif j == 7:
                string += "^"
            elif j != 1:
                string += "#"
            else:
                string += "."
        print(string)

maximum = 0
for i in range(len(X)):
    maximum = max(maximum, calculate(
        position=[i, 0], 
        direction=0
    ), calculate(
        position=[i, len(X[0]) - 1], 
        direction=2
    ))

for i in range(len(X[0])):
    maximum = max(maximum, calculate(
        position=[0, i], 
        direction=1
    ), calculate(
        position=[len(X) - 1, i], 
        direction=3
    ))

print("Part Two Answer: " + str(maximum))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # takes around 30 seconds