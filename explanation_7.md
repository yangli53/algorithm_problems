### Design

This problem is very similar as problem 5. Based on the previous solution, I will follow the instruction to make some adjustments.

### Time Complexity

The time complexity of add_handler is O(n) where n is the number of parts of a path. First, split_path function takes O(n) time to split the path. Then it takes O(n) time to insert the path. Thus the total time spent is O(n).

The time complexity of lookup is O(n). The reason is the same as above. 

### Space Complexity

The space complexity of add_handler function is O(n) because it takes n units of space to store the splitted parts and then insert them. 

The space complexity of lookup function is O(n) because it also takes n units of space to store the splitted parts.