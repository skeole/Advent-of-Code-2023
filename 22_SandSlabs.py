import math # for 2024 I'm switching to Java
from copy import deepcopy
import time
from UsefulFunctions import *
from queue import Queue

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

maxx = 0
maxy = 0
for line in file:
    first, second = line.split("~")
    first = first.split(",")
    second = second.split(",")
    for i in range(len(first)):
        first[i] = int(first[i])
        second[i] = int(second[i])
    X.append([first, second])
    maxx = max(maxx, max(first[0], second[0]))
    maxy = max(maxy, max(first[1], second[1]))


def hi(a):
    return min(a[0][2], a[1][2])

X = sortarraysonfunction(X, hi)[0]

def tick(X):

    ret = 0
    
    maxz_at_coordinates = [0] * (maxx + 1)
    for i in range(len(maxz_at_coordinates)):
        maxz_at_coordinates[i] = [0] * (maxy + 1)

    for i in X:
        maxz = maxz_at_coordinates[i[0][0]][i[0][1]]
        minz = min(i[0][2], i[1][2])
        # ex. if its 3 and 0, we can fall by 2
        if i[0][0] != i[1][0]:
            minx = min(i[0][0], i[1][0])
            maxx_ = max(i[0][0], i[1][0])
            for j in range(minx, maxx_ + 1):
                maxz = max(maxz, maxz_at_coordinates[j][i[0][1]])
            fallby = minz - maxz - 1
            i[0][2] -= fallby
            i[1][2] -= fallby
            if fallby != 0:
                ret += 1
            maxz = max(i[0][2], i[1][2])
            for j in range(minx, maxx_ + 1):
                maxz_at_coordinates[j][i[0][1]] = maxz
        else:
            miny = min(i[0][1], i[1][1])
            maxy_ = max(i[0][1], i[1][1])
            for j in range(miny, maxy_ + 1):
                maxz = max(maxz, maxz_at_coordinates[i[0][0]][j])
            fallby = minz - maxz - 1
            i[0][2] -= fallby
            i[1][2] -= fallby
            if fallby != 0:
                ret += 1
            maxz = max(i[0][2], i[1][2])
            for j in range(miny, maxy_ + 1):
                maxz_at_coordinates[i[0][0]][j] = maxz
    
    return ret

def intersects(brick1, brick2):
    minx1 = min(brick1[0][0], brick1[1][0])
    maxx1 = max(brick1[0][0], brick1[1][0])
    minx2 = min(brick2[0][0], brick2[1][0])
    maxx2 = max(brick2[0][0], brick2[1][0])
    miny1 = min(brick1[0][1], brick1[1][1])
    maxy1 = max(brick1[0][1], brick1[1][1])
    miny2 = min(brick2[0][1], brick2[1][1])
    maxy2 = max(brick2[0][1], brick2[1][1])
    minz1 = min(brick1[0][2], brick1[1][2])
    maxz1 = max(brick1[0][2], brick1[1][2])
    minz2 = min(brick2[0][2], brick2[1][2])
    maxz2 = max(brick2[0][2], brick2[1][2])
    return not (maxx1 < minx2 or minx1 > maxx2 or maxy1 < miny2 or miny1 > maxy2 or maxz1 < minz2 or minz1 > maxz2)

tick(X)
Y = deepcopy(X)

fst = 0
snd = 0

for i in range(len(Y)):
    X = deepcopy(Y)
    X.pop(i)
    v = tick(X)
    if v == 0:
        fst += 1
    else:
        snd += v

print("Part One Answer: " + str(fst))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()


print("Part Two Answer: " + str(snd)) # lmao this stupid as hell
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))