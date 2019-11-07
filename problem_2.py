def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return rotated_array_search_soln(input_list, number, 0, len(input_list) - 1)
           
def rotated_array_search_soln(array, number, start_index, end_index):
    
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index) // 2
    
    if array[mid_index] == number:
        return mid_index
    
    # if pivot is on the left of median
    if array[start_index] > array[mid_index]:
        # if target is in the right half
        if array[mid_index] < number <= array[end_index]:
            return rotated_array_search_soln(array, number, mid_index + 1, end_index)
        return rotated_array_search_soln(array, number, 0, mid_index - 1)
    
    else: # if pivot is on the right of median
        # if target is in the left half
        if array[start_index] <= number < array[mid_index]:
            return rotated_array_search_soln(array, number, 0, mid_index - 1)
        return rotated_array_search_soln(array, number, mid_index + 1, end_index)

    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")



# test case 1
print('\nTest case 1: search 2 in list []. Answer is -1.')
print(rotated_array_search([], 2))

# test case 2
print('\nTest case 2: search 2 in list [2]. Answer is 0.')
print(rotated_array_search([2], 2))

# test case 3
print('\nTest case 3: search 3 in list [2]. Answer is -1.')
print(rotated_array_search([2], 3))

# test case 4
print('\nTest case 4: search 1 in list [2, 1]. Answer is 1.')
print(rotated_array_search([2, 1], 1))

# test case 5
print('\nTest case 5: search 3 in list [2, 1]. Answer is -1.')
print(rotated_array_search([2, 1], 3))

# test case 6
print('\nTest case 6: search 1 in list [6, 7, 8, 1, 2, 3, 4]. Answer is 3.')
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))

# test case 7
print('\nTest case 7: search 8 in list [6, 7, 8, 1, 2, 3, 4]. Answer is 2.')
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))

# test case 8
print('\nTest case 8: search 10 in list [6, 7, 8, 1, 2, 3, 4]. Answer is -1.')
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))

# test case 9
print('\nTest case 9: search 6 in list [6, 7, 8, 9, 10, 1, 2, 3, 4]. Answer is 0.')
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))

# test case 10
print('\nTest case 10: search 1 in list [6, 7, 8, 9, 10, 1, 2, 3, 4]. Answer is 5.')
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))

# test case 11
print('\nTest case 11: search 6 in list [1, 3, 4, 6, 7, 8, 9, 10]. Answer is 3.')
print(rotated_array_search([1, 3, 4, 6, 7, 8, 9, 1], 6))
