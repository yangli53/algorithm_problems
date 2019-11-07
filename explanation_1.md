### Design

To achieve the time complexity of O(log(n)), I need to use binary search. I will set the start number as 0 and the end number as target number. Then I will find the median, calculate its square and compare the square number with the target number. If it equals to the target, return the median; if it is smaller than the target, traverse the right half; if it is larger than the target, traverse the left half until the square is larger than the target. Finally return the current start number minus 1. 

### Time Complexity

I used binary search so the time complexity is O(log(n)).

### Space Complexity

The space complexity is O(1) because I used iteration in this problem. In each iteration, it takes constant space; in each new iteration, the space allocated will be updated with new values. Therefore there is no need to use additional space. 