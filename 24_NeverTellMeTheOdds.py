import math
from copy import deepcopy
import time
from UsefulFunctions import *
from queue import Queue

start = time.time()
X = []

with open("0_Data.txt") as fileInput:
    file = list(fileInput)

for line in file:
    C = line.strip().split(" @ ")
    C = [C[0].split(", "), C[1].split(", ")]
    X.append([[int(C[0][0]), int(C[0][1]), int(C[0][2])], [int(C[1][0]), int(C[1][1]), int(C[1][2])]])

lower = 200000000000000
upper = 400000000000000

if len(X) == 5:
    lower = 7
    upper = 27

count = 0

for i in range(len(X) - 1):
    for j in range(i + 1, len(X)):
        first = X[i]
        second = X[j]
        x0, y0, vx0, vy0 = first[0][0], first[0][1], first[1][0], first[1][1]
        x1, y1, vx1, vy1 = second[0][0], second[0][1], second[1][0], second[1][1] # no velocities are zero :)
        m0 = vy0 / vx0
        m1 = vy1 / vx1

        ix = 0
        iy = 0

        if m0 == m1: # with the two times this happens the vxes are not the same (and obviously the vys aren't either)
            # however for this challenge we just need to see if they are aligned :D

            pass # they never happen to intersect here

        else:
            # x * (m0 - m1) = y1 - y0 + x0 * m0 - x1 * m1
            ix = (y1 - y0 + x0 * m0 - x1 * m1) / (m0 - m1)
            iy = y0 + m0 * (ix - x0)

        # now we have to make sure the ix is in the future for both!

        if ix < lower or iy < lower or ix > upper or iy > upper:
            pass # print(str(first) + " and " + str(second) + " did not intersect inside region")
        elif (ix - x0) / vx0 < 0 or (ix - x1) / vx1 < 0:
            pass # print(str(first) + " and " + str(second) + " intersected in the past")
        else:
            pass # print(str(first) + " and " + str(second) + " intersected yippee")
            count += 1
        

print("Part One Answer: " + str(count))
print("Part One Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))
start = time.time()
print()

''' Our initial point: X, Y, Z, VX, VY, VZ

Say our point is xN, yN, zN, vxN, vyN, vzN

The two paths intersect if the following are all equal:
 - xN - X / VX - vxN
 - yN - Y / VY - vyN
 - zN - Z / VZ - vzN

this means we have 6 unknowns, 2n equations --> we need n = 3 points
but wait... we have a bunch of X * VYs and stuff

The two equations we get from this:
 - (xN - X) * (VY - vyN) = (yN - Y) * (VX - vxN)
 - (xN - X) * (VZ - vzN) = (zN - Z) * (VX - vxN)
 - xN * VY - xN * vyN - X * VY + X * vyN = yN * VX - yN * vxN - Y * VX + Y * vxN
 - xN * VZ - xN * vzN - X * VZ + X * vzN = zN * VX - zN * vxN - Z * VX + Z * vxN

Rearranging, we get:
 - xN * VY - xN * vyN + X * vyN - yN * VX + yN * vxN - Y * vxN = X * VY - Y * VX
 - xN * VZ - xN * vzN + X * vzN - zN * VX + zN * vxN - Z * vxN = X * VZ - Z * VX

In other words, for all n
 - xN * VY - xN * vyN + X * vyN - yN * VX + yN * vxN - Y * vxN
 - xN * VZ - xN * vzN + X * vzN - zN * VX + zN * vxN - Z * vxN
 - are both constants

This means we still have 6 unknowns; however, we have 2 * (n - 1) equations, so we actually need n = 4 points
 - x0 * VY - x0 * vy0 + X * vy0 - y0 * VX + y0 * vx0 - Y * vx0 = xN * VY - xN * vyN + X * vyN - yN * VX + yN * vxN - Y * vxN
 - x0 * VZ - x0 * vz0 + X * vz0 - z0 * VX + z0 * vx0 - Z * vx0 = xN * VZ - xN * vzN + X * vzN - zN * VX + zN * vxN - Z * vxN
 
 - X * (vy0 - vyN) + Y * (vxN - vx0) + VX * (yN - y0) + VY * (x0 - xN) = x0 * vy0 - xN * vyN - y0 * vx0 + yN * vxN
 - X * (vz0 - vzN) + Z * (vxN - vx0) + VX * (zN - z0) + VZ * (x0 - xN) = x0 * vz0 - xN * vzN - z0 * vx0 + zN * vxN

'''

x0, y0, z0 = X[0][0]
vx0, vy0, vz0 = X[0][1]

equations = [] # format: X, Y, Z, VX, VY, VZ, constant
for i in range(1, 4):
    xN, yN, zN = X[i][0]
    vxN, vyN, vzN = X[i][1]

    equations.append([
        vy0 - vyN, vxN - vx0, 0, yN - y0, x0 - xN, 0, x0 * vy0 - xN * vyN - y0 * vx0 + yN * vxN
    ])

    equations.append([
        vz0 - vzN, 0, vxN - vx0, zN - z0, 0, x0 - xN, x0 * vz0 - xN * vzN - z0 * vx0 + zN * vxN
    ])

def determinant(matrix):

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            sign = (-1) ** i
            submatrix = [row[:i] + row[i + 1:] for row in matrix[1:]] # thanks chat gpt :D
            det += sign * matrix[0][i] * determinant(submatrix)
        return det

s = 0

for i in range(3):
    first = []
    second = []
    for j in range(6):
        first.append(equations[j][:-1])
        second.append([])
        for k in range(7):
            if k != i:
                second[j].append(equations[j][k])
    s += (-determinant(second) / determinant(first) * ((-1) ** i))


print("Part Two Answer: " + str(int(s)))
print("Part Two Runtime : " + str(int((time.time() - start) * 100 + 0.5) / 100))