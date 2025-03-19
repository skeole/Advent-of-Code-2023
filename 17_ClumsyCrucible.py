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

cache = []

def reset():
    global cache
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
    
    cache = [before_right, before_down, before_left, before_up] # based on how many rotations of [-1, 0] you need to do to go backwards
    # remember, [0, 1] is down not up

def solve(shortest_move, longest_move):
    global cache
    
    reset()
    just_reset = [[len(X) - 1, len(X[1]) - 1, 0], [len(X) - 1, len(X[1]) - 1, 1]]
    
    # [row, column, direction]

    while len(just_reset) > 0:
        just_just_reset = []
        for i in just_reset:
            rc = [i[0], i[1]]
            for j in range(4): # all the directions we can go
                if j % 2 != i[2] % 2: # if we're going in a new direction
                    for k in range(max(shortest_move, 1), longest_move + 1):
                        backwards_position = UsefulFunctions.two_d_vector_add(rc, UsefulFunctions.two_d_vector_multiply_scalar(UsefulFunctions.two_d_vector_rotate_counterclockwise([-1, 0], j), k))
                        score = cache[i[2]][i[0]][i[1]]
                        if UsefulFunctions.works(X, backwards_position):
                            for l in range(k):
                                score += UsefulFunctions.access(X, UsefulFunctions.two_d_vector_add(rc, UsefulFunctions.two_d_vector_multiply_scalar(UsefulFunctions.two_d_vector_rotate_counterclockwise([-1, 0], j), l)))
                            if score < cache[j][backwards_position[0]][backwards_position[1]]:
                                cache[j][backwards_position[0]][backwards_position[1]] = score
                                just_just_reset.append([backwards_position[0], backwards_position[1], j])
        just_reset = deepcopy(just_just_reset)
    
    return min(cache[0][0][0], cache[1][0][0])

print("Part One Answer: " + str(solve(0, 3)))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # TWO MINUTES LMAO
start = time.time()
print()

print("Part Two Answer: " + str(solve(4, 10)))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # THREE MINUTES