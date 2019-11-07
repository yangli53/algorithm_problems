### Design

To achieve the time complexity of O(log(n)), I need to use binary search. If the pivot point is on the left of the midpoint and the target is in the right half of the list, I will traverse the right half; otherwise, I will traverse the left half. If the pivot point is on the right of the midpoint and the target is in the left half, I will traverse the left half; otherwise, I will traverse the right half. 

### Time Complexity

I used binary search so the time complexity is O(log(n)).

### Space Complexity

The space complexity is O(n) because I used recursion here. In each stack frame, it takes constant space; but it should multiply the number of stack frames for the total space allocated. For the worst case, the number of stack frames can be n/2. Thus the total space complexity is O(n). 
