def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # keep track of 0's postion and 2's potion
    zero_pos = 0
    two_pos = len(input_list) - 1
    
    current_pos = 0
    
    while current_pos <= two_pos:
        # if number is 0, swap it with the number at zero_pos
        if input_list[current_pos] == 0:
            input_list[current_pos] = input_list[zero_pos]
            input_list[zero_pos] = 0
            zero_pos += 1
            current_pos += 1
        # if number is 2, swap it with the number at two_pos
        elif input_list[current_pos] == 2:
            input_list[current_pos] = input_list[two_pos]
            input_list[two_pos] = 2
            two_pos -= 1
        else:
            current_pos += 1
            
    return input_list



# test case 1
print('\nTest case 1: sort array []. Answer is []')
print(sort_012([]))

# test case 2
print('\nTest case 2: sort array [0]. Answer is [0]')
print(sort_012([0]))

# test case 3
print('\nTest case 3: sort array [2, 0]. Answer is [0, 2]')
print(sort_012([2, 0]))

# test case 4
print('\nTest case 4: sort array [0, 2, 1]. Answer is [0, 1, 2]')
print(sort_012([0, 2, 1]))

# test case 5
print('\nTest case 5: sort array [1, 1, 1]. Answer is [1, 1, 1]')
print(sort_012([1, 1, 1]))

# test case 6
print('\nTest case 6: sort array [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]. \nAnswer is [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]')
print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]))

# test case 7
print('\nTest case 7: sort array [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]. \nAnswer is [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]')
print(sort_012([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))

# test case 8
print('\nTest case 8: sort array [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]. \nAnswer is [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]')
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]))
