### Design

The bonus challenge says it is possible to find the smallest/min and largest/max integers in a single traversal, which reminds me of problem 4. But the difference is that there is no need to sort the list here. I will set the first integer as the current min and max integer. Then I will interate the list to compare each integer with min and max and reassign min and max.  

### Time Complexity

The time complexity is O(n) because this is a linear search.

### Space Complexity

The space complexity is O(1) because it takes constant space to store the value in each iteration and in each new iteration the space allocated will be updated. 