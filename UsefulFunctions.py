from copy import deepcopy

def printarray(arr):
    for i in arr:
        t = ""
        for j in i:
            t += j
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

capitalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercases = "abcdefghijklmnopqrstuvwxyz"