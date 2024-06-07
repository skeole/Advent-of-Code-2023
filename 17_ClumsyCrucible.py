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
    C = list(C)
    for i in range(len(C)):
        C[i] = int(C[i])
    X.append(C)

before_down = [99999] * (len(X))
before_right = [99999] * (len(X))
before_up = [99999] * (len(X))
before_left = [99999] * (len(X))
for i in range(len(before_down)):
    before_down[i] = [99999] * (len(X[0]))
    before_right[i] = [99999] * (len(X[0]))
    before_up[i] = [99999] * (len(X[0]))
    before_left[i] = [99999] * (len(X[0]))

before_down[-1][-1] = 0
before_right[-1][-1] = 0
before_up[-1][-1] = 0
before_left[-1][-1] = 0

def cumulative_sum(i, j, direction, length):
    count = 0
    direction = direction % 4
    for counter in range(length):
        if direction == 0: # right
            count += UsefulFunctions.get(X, i, j + 1 + counter, default_value=99999)
        elif direction == 1: # down
            count += UsefulFunctions.get(X, i + 1 + counter, j, default_value=99999)
        elif direction == 2: # left
            count += UsefulFunctions.get(X, i, j - 1 - counter, default_value=99999)
        else: # up
            count += UsefulFunctions.get(X, i - 1 - counter, j, default_value=99999)
    return count

static = False

while not static:
    static = True
    # if ANYTHING changes... static = False
    for i in range(len(X)):
        for j in range(len(X[0])):
            
            temp = before_down[i][j]
            for k in range(3):
                before_down[i][j] = min(
                    before_down[i][j], 
                    cumulative_sum(i, j, 1, k + 1) + UsefulFunctions.get(before_right, i + k + 1, j, default_value=99999), 
                    cumulative_sum(i, j, 1, k + 1) + UsefulFunctions.get(before_left, i + k + 1, j, default_value=99999), 
                )
            if temp != before_down[i][j]:
                static = False
            
            temp = before_up[i][j]
            for k in range(3):
                before_up[i][j] = min(
                    before_up[i][j], 
                    cumulative_sum(i, j, 3, k + 1) + UsefulFunctions.get(before_right, i - k - 1, j, default_value=99999), 
                    cumulative_sum(i, j, 3, k + 1) + UsefulFunctions.get(before_left, i - k - 1, j, default_value=99999), 
                )
            if temp != before_up[i][j]:
                static = False
                
            temp = before_right[i][j]
            for k in range(3):
                before_right[i][j] = min(
                    before_right[i][j], 
                    cumulative_sum(i, j, 0, k + 1) + UsefulFunctions.get(before_up, i, j + k + 1, default_value=99999), 
                    cumulative_sum(i, j, 0, k + 1) + UsefulFunctions.get(before_down, i, j + k + 1, default_value=99999), 
                )
            if temp != before_right[i][j]:
                static = False
                
            temp = before_left[i][j]
            for k in range(3):
                before_left[i][j] = min(
                    before_left[i][j], 
                    cumulative_sum(i, j, 2, k + 1) + UsefulFunctions.get(before_up, i, j - k - 1, default_value=99999), 
                    cumulative_sum(i, j, 2, k + 1) + UsefulFunctions.get(before_down, i, j - k - 1, default_value=99999), 
                )
            if temp != before_left[i][j]:
                static = False

print("Part One Answer: " + str(min(before_right[0][0], before_down[0][0])))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # TWO MINUTES LMAO
start = time.time()
print()

before_down = [99999] * (len(X))
before_right = [99999] * (len(X))
before_up = [99999] * (len(X))
before_left = [99999] * (len(X))
for i in range(len(before_down)):
    before_down[i] = [99999] * (len(X[0]))
    before_right[i] = [99999] * (len(X[0]))
    before_up[i] = [99999] * (len(X[0]))
    before_left[i] = [99999] * (len(X[0]))

before_down[-1][-1] = 0
before_right[-1][-1] = 0
before_up[-1][-1] = 0
before_left[-1][-1] = 0

static = False

while not static:
    static = True
    # if ANYTHING changes... static = False
    for i in range(len(X)):
        for j in range(len(X[0])):
            
            temp = before_down[i][j]
            for k in range(3, 10):
                before_down[i][j] = min(
                    before_down[i][j], 
                    cumulative_sum(i, j, 1, k + 1) + UsefulFunctions.get(before_right, i + k + 1, j, default_value=99999), 
                    cumulative_sum(i, j, 1, k + 1) + UsefulFunctions.get(before_left, i + k + 1, j, default_value=99999), 
                )
            if temp != before_down[i][j]:
                static = False
            
            temp = before_up[i][j]
            for k in range(3, 10):
                before_up[i][j] = min(
                    before_up[i][j], 
                    cumulative_sum(i, j, 3, k + 1) + UsefulFunctions.get(before_right, i - k - 1, j, default_value=99999), 
                    cumulative_sum(i, j, 3, k + 1) + UsefulFunctions.get(before_left, i - k - 1, j, default_value=99999), 
                )
            if temp != before_up[i][j]:
                static = False
                
            temp = before_right[i][j]
            for k in range(3, 10):
                before_right[i][j] = min(
                    before_right[i][j], 
                    cumulative_sum(i, j, 0, k + 1) + UsefulFunctions.get(before_up, i, j + k + 1, default_value=99999), 
                    cumulative_sum(i, j, 0, k + 1) + UsefulFunctions.get(before_down, i, j + k + 1, default_value=99999), 
                )
            if temp != before_right[i][j]:
                static = False
                
            temp = before_left[i][j]
            for k in range(3, 10):
                before_left[i][j] = min(
                    before_left[i][j], 
                    cumulative_sum(i, j, 2, k + 1) + UsefulFunctions.get(before_up, i, j - k - 1, default_value=99999), 
                    cumulative_sum(i, j, 2, k + 1) + UsefulFunctions.get(before_down, i, j - k - 1, default_value=99999), 
                )
            if temp != before_left[i][j]:
                static = False

print("Part Two Answer: " + str(min(before_right[0][0], before_down[0][0])))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # THREE MINUTES