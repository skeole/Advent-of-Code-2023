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
    C = list(C)
    for i in range(len(C)):
        C[i] = int(C[i])
    X.append(C)

cache = []

def reset():
    global cache
    before_vertical = [99999] * (len(X))
    before_horizontal = [99999] * (len(X))
    for i in range(len(before_vertical)):
        before_vertical[i] = [99999] * (len(X[0]))
        before_horizontal[i] = [99999] * (len(X[0]))

    before_vertical[-1][-1] = 0
    before_horizontal[-1][-1] = 0
    
    cache = [before_vertical, before_horizontal] # based on how many rotations of [-1, 0] you need to do to go backwards
    # remember, [0, 1] is down not up

def solve(shortest_move, longest_move):
    global cache
    reset()
    
    size = 2000000 # 2 million
    q = [0] * size
    q[0] = [len(X) - 1, len(X[1]) - 1, 0]
    q[1] = [len(X) - 1, len(X[1]) - 1, 1]
    index = 0 # next one we access
    jndex = 2 # next one we add to
    
    # [row, column, direction]

    while q[index] != 0:
        rc = [q[index][0], q[index][1]]
        base_score = cache[q[index][2]][q[index][0]][q[index][1]]
        
        j = 1 - (q[index][2] % 2)
        for k in range(max(shortest_move, 1), longest_move + 1):
            backwards_position = two_d_vector_add(rc, two_d_vector_multiply_scalar(two_d_vector_rotate_counterclockwise([-1, 0], j), k))
            if works(X, backwards_position):
                score = base_score
                for l in range(k):
                    score += access(X, two_d_vector_add(rc, two_d_vector_multiply_scalar(two_d_vector_rotate_counterclockwise([-1, 0], j), l)))
                if score < cache[j][backwards_position[0]][backwards_position[1]]:
                    cache[j][backwards_position[0]][backwards_position[1]] = score
                    q[jndex] = [backwards_position[0], backwards_position[1], j]
                    jndex += 1
                    jndex = jndex % size
            else:
                break
        
        for k in range(max(shortest_move, 1), longest_move + 1):
            backwards_position = two_d_vector_add(rc, two_d_vector_multiply_scalar(two_d_vector_rotate_counterclockwise([1, 0], j), k))
            if works(X, backwards_position):
                score = base_score
                for l in range(k):
                    score += access(X, two_d_vector_add(rc, two_d_vector_multiply_scalar(two_d_vector_rotate_counterclockwise([1, 0], j), l)))
                if score < cache[j][backwards_position[0]][backwards_position[1]]:
                    cache[j][backwards_position[0]][backwards_position[1]] = score
                    q[jndex] = [backwards_position[0], backwards_position[1], j]
                    jndex += 1
                    jndex = jndex % size
            else:
                break

        q[index] = 0
        index += 1
        index = index % size # if appending only makes it ~20% faster whats the other 80%
    
    return min(cache[0][0][0], cache[1][0][0])

print("Part One Answer: " + str(solve(0, 3)))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # 1244 - 15 seconds
start = time.time()
print()

print("Part Two Answer: " + str(solve(4, 10)))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # 1367 - 30 seconds
