import math
from copy import deepcopy
import time
from UsefulFunctions import *
from queue import Queue

start = time.time()
X = []

broadcast_to = []
module_names = []
modules = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    first, second = line.strip().split(" -> ")
    second = second.split(", ")
    
    if first[0] == "%": # false, current state, recipients

        first = first[1:]
        module_names.append(first)
        recipients_temp = []
        for i in second:
            recipients_temp.append(i)
        
        modules.append([False, False, recipients_temp])

    elif first[0] == "&": # true, receivers, recipients, received values, active

        first = first[1:]
        module_names.append(first)
        recipients_temp = []
        for i in second:
            recipients_temp.append(i)
        modules.append([True, [], recipients_temp, [], 0])

    else:

        for i in second:
            broadcast_to.append(i)

for i in range(len(broadcast_to)):
    broadcast_to[i] = module_names.index(broadcast_to[i])

target_module_index = -1

for i in range(len(modules)):

    for j in range(len(modules[i][2])): # iterate over all receipients
        if (modules[i][2][j] in module_names):
            modules[i][2][j] = module_names.index(modules[i][2][j]) # replace with index
            if modules[modules[i][2][j]][0]: # if it is being sent to a & module
                modules[modules[i][2][j]][1].append(i)
        else:
            modules[i][2][j] = -1
            target_module_index = i

target = len(module_names)
for i in modules:
    if i[0]: # &
        i[3] = [True] * target
        i[4] = target
        for j in i[1]:
            if i[3][j]:
                i[3][j] = False
                i[4] -= 1

signal_counts = [0, 0]
number_of_presses = 0
q = Queue() # .qsize, .get, .put

def press():
    global number_of_presses, signal_counts
    number_of_presses += 1
    signal_counts[0] += 1
    for i in broadcast_to:
        q.put([i, False]) # False = low

high = 0
low = 0

part_one_time = 0

product = 1
numbers = 0

press()
while True: # [recipient, value, sender]
    if (q.qsize() == 0):
        if number_of_presses == 1000:
            high = signal_counts[1]
            low = signal_counts[0]
            part_one_time = time.time()
        press()

    temp = q.get()

    if temp[1]:
        signal_counts[1] += 1
    else:
        signal_counts[0] += 1
    
    if temp[0] == -1: # output press
        pass
    elif modules[temp[0]][0]: # &

        if not modules[temp[0]][3][temp[2]] and temp[1]:
            modules[temp[0]][3][temp[2]] = True
            modules[temp[0]][4] += 1
        elif modules[temp[0]][3][temp[2]] and not temp[1]:
            modules[temp[0]][3][temp[2]] = False
            modules[temp[0]][4] -= 1
        
        for j in modules[temp[0]][2]:
            q.put([j, modules[temp[0]][4] != target, temp[0]])
            if j == target_module_index and modules[temp[0]][4] != target:
                product *= number_of_presses
                numbers += 1

    else: # % 

        if not temp[1]:

            modules[temp[0]][1] = not modules[temp[0]][1]
            for j in modules[temp[0]][2]:
                q.put([j, modules[temp[0]][1], temp[0]])
                if j == target_module_index and modules[temp[0]][1]:
                    product *= number_of_presses
                    numbers += 1
    
    if numbers == 4:
        break

print("Part One Answer: " + str(high * low))
print("Part One Runtime : " + str(int((part_one_time - start) * 100 + 0.5) / 100))
start = time.time()
print()

print("Part Two Answer: " + str(product)) # ima be honest i would not have gotten this myself
print("Part Two Runtime : " + str(int((time.time() - part_one_time) * 100 + 0.5) / 100))