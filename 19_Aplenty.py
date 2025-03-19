import math
from copy import deepcopy
import time
from UsefulFunctions import *

start = time.time()

with open("2023/0_Data.txt") as fileInput:
    file = list(fileInput)

first = True
instructions = []
temp_instructions = []
program_names = []
xmas_entries = []
for line in file:
    C = line.strip()
    if C == "":
        first = False
    elif first:
        temp = C.split("{")
        program_names.append(temp[0])
        temp[1] = temp[1].strip("}")
        temp[1] = temp[1].split(",")
        temp_instructions.append(temp[1])
    else:
        temp = C.strip("{}")
        temp = temp.split(",")
        vals = []
        for i in temp:
            vals.append(int(i[i.index("=") + 1:]))
        xmas_entries.append(vals)

success = len(program_names)
program_names.append("A")
failure = len(program_names)
program_names.append("R")

for i in temp_instructions:
    temp_instruction = []
    for j in range(len(i) - 1):
        temporary = i[j].split(":")
        greater_than = temporary[0][1] == ">"

        temp_instruction.append(["xmas".index(temporary[0][0]), greater_than, int(temporary[0][2:]), program_names.index(temporary[1])])
    temp_instruction.append([program_names.index(i[-1])])
    instructions.append(temp_instruction)

starting_index = program_names.index("in")

total_sum = 0
for i in xmas_entries:
    index = starting_index
    while True:
        for j in instructions[index]:
            if len(j) == 1:
                index = j[0]
                break
            else:
                if (i[j[0]] != j[2]) and ((i[j[0]] > j[2]) == j[1]):
                    index = j[3]
                    break
        if index == success:
            total_sum += i[0] + i[1] + i[2] + i[3]
            break
        elif index == failure:
            break

print("Part One Answer: " + str(total_sum))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

# not too bad, we just have to see which of each character leads to A and which ones lead to R - no need to iterate

def single_range_intersection(first_range, second_range):
    if first_range[1] < second_range[0]:
        return []
    if first_range[0] > second_range[1]:
        return []
    return [max(first_range[0], second_range[0]), min(first_range[1], second_range[1])]

def range_intersections(ranges, new_range): # ranges must be sorted, i.e. [1, 2], [4, 6] not [4, 6], [1, 2]
    new_ranges = []
    for i in ranges:
        if len(single_range_intersection(i, new_range)) != 0:
            new_ranges.append(single_range_intersection(i, new_range))
    return new_ranges

accepted = [success, [[1, 4000]], [[1, 4000]], [[1, 4000]], [[1, 4000]], []]

# plan: keep iterating through until you get to the starting index
# shouldn't be any overlap - completely determinitive

def unravel(data): # data structure: [index, [x ranges], [m ranges], [a ranges], [s ranges], [previouses]]
    unravels = []
    previouses = deepcopy(data[5])
    previouses.append(index)
    for i in range(len(instructions)): # If there's recursion add prevs to the data structure
        if i not in previouses:
            current_ranges = deepcopy([data[1], data[2], data[3], data[4]])
            for j in instructions[i]:
                if j[-1] == data[0]:
                    adjusted_ranges = deepcopy(current_ranges)
                    if (len(j) != 1) and (len(range_intersections(adjusted_ranges[j[0]], ([j[2] + 1, 4000] if j[1] else [1, j[2] - 1]))) != 0):
                        adjusted_ranges[j[0]] = range_intersections(adjusted_ranges[j[0]], ([j[2] + 1, 4000] if j[1] else [1, j[2] - 1]))
                    unravels.append(deepcopy([i, adjusted_ranges[0], adjusted_ranges[1], adjusted_ranges[2], adjusted_ranges[3], previouses]))
                if len(j) != 1:
                    current_ranges[j[0]] = range_intersections(current_ranges[j[0]], ([1, j[2]] if j[1] else [j[2], 4000]))
    return unravels

# we need to push to q until we get all of them in
q = []
ueue = [accepted]
while len(ueue) > 0:
    for i in unravel(ueue.pop(0)):
        if i[0] == starting_index:
            q.append(i)
        else:
            ueue.append(i)

count = 0
for i in q:
    mult = 1
    for j in range(1, 5):
        summer = 0
        for k in i[j]:
            summer += k[1] - k[0] + 1
        mult *= summer
    count += mult

print("Part Two Answer: " + str(count))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100)) # 12 seconds, kinda slow ngl