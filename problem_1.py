def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    try:
        assert isinstance(number, int)
        
        if number < 0:
            return print('Invalid number!')

        # assign a start number of 0 and an end number of target
        start_num = 0
        end_num = number

        while start_num <= end_num:
            # find median and calculate its square
            mid_num = (start_num + end_num) // 2
            squared = mid_num * mid_num

            # compare square with target 
            # if it equals to target, return median
            if squared == number:
                return mid_num

            # if it is smaller than target, change start number to median + 1
            elif squared < number:
                start_num = mid_num + 1

            # if it is larger than target, change end number to median - 1
            else:
                end_num = mid_num - 1

        return start_num - 1

    except AssertionError:
        print('Number type is not an integer.')



# test case 1
print('\nTest case 1: find the square root of 0. Answer is 0.')
print(sqrt(0))

# test case 2
print('\nTest case 2: find the square root of 1. Answer is 1.')
print(sqrt(1))

# test case 3
print('\nTest case 3: find the square root of 4. Answer is 2.')
print(sqrt(4))

# test case 4
print('\nTest case 4: find the square root of 27. Answer is 5.')
print(sqrt(27))

# test case 5
print('\nTest case 5: find the square root of 9999. Answer is 99.')
print(sqrt(9999))

# test case 6
print('\nTest case 6: find the square root of -1. Answer is \"Invalid number!\"')
print(sqrt(-1))

# test case 7
print('\nTest case 7: find the square root of a. Answer is \"Number type is not an integer.\"')
print(sqrt('a'))

# test case 8
print('\nTest case 8: find the square root of 1.5. Answer is \"Number type is not an integer.\"')
print(sqrt(1.5))

