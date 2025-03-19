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
    C = C.split()
    C[0] = C[0].split(".")
    
    for i in range(len(C[0]) - 2, 0, -1): # need to keep end and start periods for part 2
        if len(C[0][i]) == 0:
            C[0].pop(i)
    
    ovr = ""
    for i in C[0]:
        ovr += i
        ovr += "."
    
    C[0] = ovr[:-1]
    C[1] = C[1].split(",")
    for i in range(len(C[1])):
        C[1][i] = int(C[1][i])
    X.append(C)

base = 0
cached_scores = []
maximum_length = 0

def solve(hotspring, code, reset_cache = True):
    global cached_scores, base, maximum_length
    if (reset_cache): # we have to start by resetting the cache, obviously
        cached_scores = [-1] * (len(hotspring) + 1) * (len(code) + 1)
        # ex if hotspring is 12, code is 3 --> can have 52
        # hotspring of 1, code of 0 -> 4
        # hotspring of 12, code of 3 -> 51
        base = len(code) + 1
        maximum_length = 0
        for i in range(len(hotspring) - 1, -1, -1):
            if hotspring[i] == "#":
                break
            else:
                maximum_length += 1
        # can have up to len(hotspring) * len(code)

    cache_index = base * len(hotspring) + len(code)

    if len(code) == 0: # don't need to cache anything here
        if len(hotspring) > maximum_length:
            return 0
        else:
            return 1
    
    if len(hotspring) == 0: # don't need to cache anything here
        return 0

    if cached_scores[cache_index] != -1:
        return cached_scores[cache_index]
    
    # what happens if we do start the next run here
    run_length = code[0]
    
    true_works = run_length < len(hotspring) + 1
    hotspring_if_true = hotspring
    code_if_true = code
    
    if true_works:
        for i in range(run_length):
            if hotspring[i] == ".":
                true_works = False
        
        if run_length < len(hotspring) and hotspring[run_length] == "#":
            true_works = False

        hotspring_if_true = hotspring[run_length + 1:]
        code_if_true = code[1:]
    
    true_val = 0
    if true_works:
        true_val = solve(hotspring_if_true, code_if_true, reset_cache = False)
    
    # what happens if we do not start the next run here
    false_works = hotspring[0] != "#"
    hotspring_if_false = hotspring[1:]
    code_if_false = code
    
    false_val = 0
    if false_works:
        false_val = solve(hotspring_if_false, code_if_false, reset_cache = False)
    
    cached_scores[cache_index] = true_val + false_val
    return true_val + false_val

counts = 0
for i in X:
    counts += solve(i[0], i[1])

print("Part One Answer: " + str(counts))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

# unfold

for i in range(len(X)):
    first = ""
    second = []
    for j in range(5):
        first += X[i][0] + "?"
        for k in X[i][1]:
            second.append(k)
    first = first[:-1]
    X[i] = [first, second]

counts = 0
for i in X:
    counts += solve(i[0], i[1])

print("Part Two Answer: " + str(counts))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # takes around .4 seconds :)