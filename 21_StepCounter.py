import math
from copy import deepcopy
import time
import UsefulFunctions
from tqdm import tqdm as tqdm

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

starting_position = 0
for line in file:
    C = line.strip()
    if "S" in C:
        starting_position = [len(X), C.index("S")]
    X.append(list(C))

X[starting_position[0]][starting_position[1]] = "."

base_plot = [0] * len(X)
for i in range(len(base_plot)):
    base_plot[i] = [-1] * len(X[0])

plot = deepcopy(base_plot)

def astar(starting_position, array_to_fill):
    boolean = True
    counter = 0
    array_to_fill[starting_position[0]][starting_position[1]] = 0
    next_list = [starting_position]
    while boolean:
        boolean = False
        counter += 1
        next_next_list = []
        for i in next_list:
            if i[0] > 0 and array_to_fill[i[0] - 1][i[1]] == -1 and X[i[0] - 1][i[1]] == ".":
                next_next_list.append([i[0] - 1, i[1]])
                array_to_fill[i[0] - 1][i[1]] = counter
                boolean = True
            if i[0] < len(X) - 1 and array_to_fill[i[0] + 1][i[1]] == -1 and X[i[0] + 1][i[1]] == ".":
                next_next_list.append([i[0] + 1, i[1]])
                array_to_fill[i[0] + 1][i[1]] = counter
                boolean = True
            if i[1] > 0 and array_to_fill[i[0]][i[1] - 1] == -1 and X[i[0]][i[1] - 1] == ".":
                next_next_list.append([i[0], i[1] - 1])
                array_to_fill[i[0]][i[1] - 1] = counter
                boolean = True
            if i[1] < len(X) - 1 and array_to_fill[i[0]][i[1] + 1] == -1 and X[i[0]][i[1] + 1] == ".":
                next_next_list.append([i[0], i[1] + 1])
                array_to_fill[i[0]][i[1] + 1] = counter
                boolean = True
        next_list = deepcopy(next_next_list)

astar(starting_position, plot)

count = 0
for i in plot:
    for j in i:
        if j % 2 == 0 and j < 65 and j > -1:
            count += 1

print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # not 5 minutes anymore
start = time.time()
print()

# I think we need to make one for all 8 corners / midsides...
# top_right: based on bottom left corner, but what we consider when going to the top and to the right

first = int((len(X) + 1) / 2)

def count_ltet(list, ltet): # 0 for even, 1 for odd
    count = 0
    for i in list:
        for j in i:
            if j <= ltet and j >= 0 and j % 2 == ltet % 2:
                count += 1
    return count

def linear_count(list, individual_steps, type): # type 0 -> directional, type 1 -> not directional
    
    if individual_steps < 0:
        return 0
    
    # parity = same as parity of type
    increment = len(list)
    maximum_steps = 0
    for i in list:
        for j in i:
            maximum_steps = max(j, maximum_steps)
    
    full_steps = max(int((individual_steps - maximum_steps) / increment) + 1, 0)
    total_steps = int(individual_steps / increment) + 1
    
    # if total steps is 9, increment is 3, max is 5
    # full steps -> 2, remaining total steps --> 4
    
    complete_first = count_ltet(list, individual_steps)
    complete_second = count_ltet(list, individual_steps + increment)
    
    count = 0
    if type == 0:
        # for the first type: int((n + 1) / 2)
        # for the second type: int(n / 2)
        count += int((full_steps + 1) / 2) * complete_first + int(full_steps / 2) * complete_second
        
        for i in range(full_steps, total_steps):
            number = count_ltet(list, individual_steps - increment * i)
            count += number
    else:
        # n is the total number
        # for the first type: int((n + 1) / 2) * int((n + 1) / 2)
        # for the second type: int(n / 2) * (int(n / 2) + 1)
        count += int((full_steps + 1) / 2) * int((full_steps + 1) / 2) * complete_first + int(full_steps / 2) * (int(full_steps / 2) + 1) * complete_second
        
        for i in range(full_steps, total_steps):
            number = count_ltet(list, individual_steps - increment * i)
            count += (i + 1) * number
    
    return count

right = deepcopy(base_plot)
astar([starting_position[0], 0], right)

top = deepcopy(base_plot)
astar([len(X) - 1, starting_position[1]], top)

left = deepcopy(base_plot)
astar([starting_position[0], len(X[0]) - 1], left)

bottom = deepcopy(base_plot)
astar([0, starting_position[1]], bottom)

top_right = deepcopy(base_plot)
astar([len(X) - 1, 0], top_right)

top_left = deepcopy(base_plot)
astar([len(X) - 1, len(X[0]) - 1], top_left)

bottom_left = deepcopy(base_plot)
astar([0, len(X[0]) - 1], bottom_left)

bottom_right = deepcopy(base_plot)
astar([0, 0], bottom_right)

steps = 26501365 # idk if this is for everyone or just my specific input

total = count_ltet(plot, steps)
total += linear_count(top, steps - first, 0)
total += linear_count(right, steps - first, 0)
total += linear_count(left, steps - first, 0)
total += linear_count(bottom, steps - first, 0)
total += linear_count(top_right, steps - first * 2, 1)
total += linear_count(top_left, steps - first * 2, 1)
total += linear_count(bottom_right, steps - first * 2, 1)
total += linear_count(bottom_left, steps - first * 2, 1)

print("Part Two Answer: " + str(total))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # 0.5 seconds
# answer should be: 609708004316870

# for smaller numbers:
    # 65: 3770
    # 196: 33665
    # 327: 93356
    # 458: 182843