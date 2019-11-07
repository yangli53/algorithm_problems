def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    
    # assign the first int as current max_int and min_int
    max_int = ints[0]
    min_int = ints[0]
    
    # compare following ints with the first int and reassign max_int and min_int 
    for num in ints:
        if num > max_int:
            max_int = num
        if num < min_int:
            min_int = num
    
    return min_int, max_int



# test case 1
print('\nTest case 1: get min and max from list []. Answer is None.')
print(get_min_max([]))

# test case 2
print('\nTest case 2: get min and max from list [2]. Answer is (2, 2).')
print(get_min_max([2]))

# test case 3
print('\nTest case 3: get min and max from list [2, 1]. Answer is (1, 2).')
print(get_min_max([2, 1]))

# test case 4
print('\nTest case 4: get min and max from list [1, 1]. Answer is (1, 1).')
print(get_min_max([1, 1]))

# test case 5
print('\nTest case 5: get min and max from list [1, 1, 0]. Answer is (0, 1).')
print(get_min_max([1, 1, 0]))

# test case 6
print('\nTest case 6: get min and max from list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. \nAnswer is (1, 10).')
print(get_min_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# test case 7
print('\nTest case 7: get min and max from list [60, 12, 78, 64, 35, 16, 0, 8, 201, 55]. \nAnswer is (0, 201).')
print(get_min_max([60, 12, 78, 64, 35, 16, 0, 8, 201, 55]))