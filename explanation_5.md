### Design

Class Trie is very similar as the one we built in class. For function "suffixes" in class TrieNode, I will use recursion to collect suffixes.

### Time Complexity

The time complexity of insert is O(n) where n is the length of a word. 

The time complexity of find in class Trie is also O(n). 

The time complexity of suffixes is O(n*m) where n is the length of the longest suffixes and m is the number of suffixes. 

### Space Complexity

The space complexity of insert is O(n) because it needs n units of space to store the word. 

The space complexity of find is O(1) because it takes constant space to store the current node.

The space complexity of suffixes is O(n*m). For each stack frame, it takes constant space to store current suffixes. It should mutiply n to store the longest suffixes. This number should again mutiply m to store all suffixes. Thus the total space allocated is O(n*m).
