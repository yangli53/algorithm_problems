def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return []
    
    if len(input_list) == 1:
        return input_list
    
    # use max_heap to sort input_list
    max_heap = MaxHeap()
    for element in input_list:
        max_heap.insert(element)
            
    # take numbers one by one to form two numbers
    num_1 = ''
    num_2 = ''
    
    for i in range(max_heap.size()):
        if i % 2 == 0:
            num_1 += str(max_heap.remove())
        else:
            num_2 += str(max_heap.remove())
    
    return [int(num_1), int(num_2)]

class MaxHeap:
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0
    
    def insert(self, data):
        self.cbt[self.next_index] = data
        
        self.up_heapify()
        
        self.next_index += 1
        
        # double the array size if capacity is full
        if self.next_index >= len(self.cbt):
            old_array = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]
            
            for i in range(len(old_array)):
                self.cbt[i] = old_array[i]
        
    def up_heapify(self):
        child_index = self.next_index
        
        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]
            
            if parent_element < child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                
                child_index = parent_index
            else:
                break
    
    def size(self):
        return self.next_index
    
    def remove(self):
        if self.size() == 0:
            return None
        
        self.next_index -= 1
        
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        
        self.cbt[0] =  last_element
        self.cbt[self.next_index] = to_remove
        
        self.down_heapify()
        
        return to_remove
    
    def down_heapify(self):
        parent_index = 0
        
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            
            parent = self.cbt[parent_index]
            left_child = None
            right_child = None
            
            max_element = parent
            
            # check if left child and right child exist
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]
                
            # compare with left child and right child
            if left_child is not None:
                max_element = max(parent, left_child)
            
            if right_child is not None:
                max_element = max(max_element, right_child)
            
            # check if parent is in the right position
            if max_element == parent:
                return 
            
            if max_element == left_child:
                self.cbt[parent_index] = max_element
                self.cbt[left_child_index] = parent
                parent_index = left_child_index
                
            if max_element == right_child:
                self.cbt[parent_index] = max_element
                self.cbt[right_child_index] = parent
                parent_index = right_child_index



print('Rearrange array elements to form two number such that their sum is maximum.')
# test case 1
print('\nTest case 1: input_list = []. Answer is []')
print(rearrange_digits([]))

# test case 2
print('\nTest case 2: input_list = [2]. Answer is [2]')
print(rearrange_digits([2]))

# test case 3
print('\nTest case 3: input_list = [1, 2]. Answer is [2, 1]')
print(rearrange_digits([1, 2]))

# test case 4
print('\nTest case 4: input_list = [1, 2, 3]. Answer is [31, 2]')
print(rearrange_digits([1, 2, 3]))

# test case 5
print('\nTest case 5: input_list = [1, 2, 3, 2, 1]. Answer is [321, 21]')
print(rearrange_digits([1, 2, 3, 2, 1]))

# test case 6
print('\nTest case 6: input_list = [4, 6, 2, 5, 9, 8]. Answer is [964, 852]')
print(rearrange_digits([4, 6, 2, 5, 9, 8]))

# test case 7
print('\nTest case 7: input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]. \nAnswer is [9753210, 864210]')
print(rearrange_digits([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]))
