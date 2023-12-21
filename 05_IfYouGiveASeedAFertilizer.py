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
    X.append(C)

seeds = []

X[0] = X[0].split()
X[0].pop(0)

seeds = deepcopy(X[0])
for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

r = deepcopy(seeds)

seeds.sort()

X.pop(0)

mappings = []

def funky_function(arr):
    return arr[0]

for i in X:
    i = i.split()
    if len(i) == 3:
        i[0] = int(i[0])
        i[1] = int(i[1])
        i[2] = int(i[2])
        mappings[-1].append([i[1], i[1] + i[2] - 1, i[0] - i[1]])
    elif len(i) == 0:
        mappings.append([])

for i in range(len(mappings)):
    mappings[i] = UsefulFunctions.sortarraysonfunction(mappings[i], funky_function)[0]

for i in range(len(mappings)):
    for j in range(len(mappings[i]) - 1, 0, -1):
        if mappings[i][j][0] - mappings[i][j - 1][1] != 1:
            mappings[i].insert(j, [mappings[i][j - 1][1] + 1, mappings[i][j][0] - 1, 0])

def combine_maps(map_one_array, map_two_array): # format of maps: initial, final, change
        
    ''' PLAN OF ATTACK
    
    Partition each map_one_array mapping by the map_two_array lines and make a new mapping for each one
    Then, remove those x values from the map_two_array mappings, and preserve those ones
    
    '''
    
    for j in range(len(map_one_array) - 1, 0, -1):
        if map_one_array[j][0] - map_one_array[j - 1][1] != 1:
            map_one_array.insert(j, [map_one_array[j - 1][1] + 1, map_one_array[j][0] - 1, 0])
    
    for j in range(len(map_two_array) - 1, 0, -1):
        if map_two_array[j][0] - map_two_array[j - 1][1] != 1:
            map_two_array.insert(j, [map_two_array[j - 1][1] + 1, map_two_array[j][0] - 1, 0])
    
    zone_read = []
    for i in map_two_array:
        zone_read.append([i[0], i[2]])
    zone_read.append([map_two_array[-1][1] + 1, 0])
    
    first_inversion = []
    for i in map_one_array:
        first_inversion.append([i[0] + i[2], i[1] + i[2], -i[2]])
    first_inversion = UsefulFunctions.sortarraysonfunction(first_inversion, funky_function)[0]
    
    for j in range(len(first_inversion) - 1, 0, -1):
        if first_inversion[j][0] - first_inversion[j - 1][1] != 1:
            first_inversion.insert(j, [first_inversion[j - 1][1] + 1, first_inversion[j][0] - 1, 0])
    
    variable_two = []
    for i in first_inversion:
        variable_two.append([i[0], i[2]])
    variable_two.append([first_inversion[-1][1] + 1, 0])
    
    combined_mapping = []
        
    first_contribution = 0
    second_contribution = 0
    
    maximum = max(zone_read[-1][0], variable_two[-1][0]) - 1
    
    zone_read.append([maximum + 1, 0])
    variable_two.append([maximum + 1, 0])
    
    # if first_contribution is 48, second_contribution is 39, number is 50: we map 50 + 48 by -48 + 39
    
    while zone_read[0][0] < maximum or variable_two[0][0] < maximum:
        if zone_read[0][0] < variable_two[0][0]:
            second_contribution = zone_read[0][1]
            lower = zone_read[0][0]
            upper = min(zone_read[1][0], variable_two[0][0], maximum + 1) - 1
            zone_read.pop(0)
        else:
            first_contribution = variable_two[0][1]
            lower = variable_two[0][0]
            upper = min(variable_two[1][0], zone_read[0][0], maximum + 1) - 1
            variable_two.pop(0)
        
        if not upper < lower:
            combined_mapping.append([lower + first_contribution, upper + first_contribution, second_contribution - first_contribution])
        
    combined_mapping = UsefulFunctions.sortarraysonfunction(combined_mapping, funky_function)[0]
    return combined_mapping

combined_map = combine_maps(mappings[0], mappings[1])

for i in range(2, len(mappings)):
    combined_map = combine_maps(combined_map, mappings[i])

def mapping(seed_number):
    if seed_number < combined_map[0][0]:
        return seed_number
    for i in combined_map:
        if not i[1] < seed_number:
            return seed_number + i[2]
    return seed_number

min_seed_mapping = mapping(seeds[0])
for i in seeds:
    min_seed_mapping = min(min_seed_mapping, mapping(i))

print("Part One Answer: " + str(min_seed_mapping))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

acceptable_range = []

for i in range(int(len(r) / 2)):
    acceptable_range.append([r[2 * i], r[2 * i] + r[2 * i + 1] - 1])

acceptable_range = UsefulFunctions.sortarraysonfunction(acceptable_range, funky_function)[0]

minimum = 1000000000000000

for i in combined_map:
    for j in acceptable_range:
        if j[0] <= i[0] and i[0] <= j[1]:
            minimum = min(minimum, i[0] + i[2])
        if i[0] <= j[0] and j[0] <= i[1]:
            minimum = min(minimum, j[0] + i[2])

print("Part Two Answer: " + str(minimum))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))