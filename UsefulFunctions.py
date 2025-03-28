from copy import deepcopy

def printarray(arr):
    for i in arr:
        t = ""
        for j in i:
            t += j
        print(t)

def printarraynumbers(arr):
    maxlen = 0
    for i in arr:
        for j in i:
            if len((str(j))) > maxlen:
                maxlen = len((str(j)))
    maxlen += 1
    for i in arr:
        t = ""
        for j in i:
            t += str(j)
            for k in range(maxlen - len(str(j))):
                t += " "
        print(t)

def combine(first, pivot, second): # should go in form of [[arrays], [values]]
    combined_list = [[], []]
    for i in first[0]:
        combined_list[0].append(deepcopy(i))
    for i in first[1]:
        combined_list[1].append(deepcopy(i))
        
    combined_list[0].append(deepcopy(pivot[0]))
    combined_list[1].append(deepcopy(pivot[1]))
    
    for i in second[0]:
        combined_list[0].append(deepcopy(i))
    for i in second[1]:
        combined_list[1].append(deepcopy(i))
    
    return combined_list

def sortarraysonvalues(list_of_arrays, list_of_values):
    assert len(list_of_arrays) == len(list_of_values)
    
    if len(list_of_arrays) < 2:
        return [list_of_arrays, list_of_values]
    
    first_list_of_values = []
    first_list_of_arrays = []
    
    second_list_of_values = []
    second_list_of_arrays = []
    
    pivot_value = list_of_values[-1]
    pivot_array = list_of_arrays[-1]
    
    for i in range(len(list_of_values) - 1):
        if list_of_values[i] > pivot_value:
            second_list_of_values.append(list_of_values[i])
            second_list_of_arrays.append(list_of_arrays[i])
        else:
            first_list_of_values.append(list_of_values[i])
            first_list_of_arrays.append(list_of_arrays[i])
        
    return combine(sortarraysonvalues(first_list_of_arrays, first_list_of_values), [pivot_array, pivot_value], sortarraysonvalues(second_list_of_arrays, second_list_of_values))
    # should go in form of [[arrays], [values]]

def sortarraysonfunction(list_of_arrays, function): # ex. function can be to return X[1]
    new_array = []
    for i in list_of_arrays:
        new_array.append(function(i))
    return sortarraysonvalues(list_of_arrays, new_array)

def choose(n, r):
    prod = 1
    for i in range(n, n - r, -1):
        prod *= i
    for i in range(1, r + 1):
        prod /= i
    return round(prod)

def binary_insert(list, element, comparison): # list must already be ordered
    pass

def binary_search(list, element, comparison): # list must be ordered
    pass

capitalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercases = "abcdefghijklmnopqrstuvwxyz"
ASCII_MINUS_32 = " !\"#$%&\'()*+,-./0123456789:;<=>?@" + capitalphabet + "[\\]^_`" + lowercases + "{|}~"

def to_ascii(character):
    return 32 + ASCII_MINUS_32.index(character)

def get(array, row, column, default_value=0):
    if row < 0 or column < 0 or row > len(array) - 1 or column > len(array[0]) - 1:
        return default_value
    return array[row][column]

def two_d_vector_add(vec_one, vec_two):
    return [vec_one[0] + vec_two[0], vec_one[1] + vec_two[1]]

def two_d_vector_multiply_scalar(vec_one, scalar):
    return [vec_one[0] * scalar, vec_one[1] * scalar]

def two_d_vector_rotate_counterclockwise(vector, number_of_nineties):
    if number_of_nineties % 4 == 1:
        return [-vector[1], vector[0]]
    elif number_of_nineties % 4 == 2:
        return [-vector[0], -vector[1]]
    elif number_of_nineties % 4 == 3:
        return [vector[1], -vector[0]]
    else:
        return [vector[0], vector[1]]

def works(array, vector_row_column):
    if vector_row_column[0] < 0 or vector_row_column[1] < 0 or vector_row_column[0] > len(array) - 1 or vector_row_column[1] > len(array[0]) - 1:
        return False
    return True

def access(array, vector_row_column):
    return array[vector_row_column[0]][vector_row_column[1]]

def modify(array, vector_row_column, new_value):
    array[vector_row_column[0]][vector_row_column[1]] = new_value