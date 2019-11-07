### Design

I need to sort the list from max to min and then take the number one by one to form two numbers. I was thinking about merge sort because the time complexity is O(nlog(n)) but then I realize heapsort is more effecient because heapsort saves space. 

I will create a class of MaxHeap and use its function "insert" to sort the list. Then I will use function "remove" to take each number to form two numbers. 

### Time Complexity

The time complexity of MaxHeap insertion is O(nlog(n)) where n is the size of the input list. The time complexity of MaxHeap removal is O(nlog(n)). Thus the total time complexity is O(nlog(n)). 

### Space Complexity

The space complexity is O(n) because it needs n units of space to store the array.

