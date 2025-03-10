# NOTES

## Data Structures
- Trees
  - BST
- Tries
- Stack / Queue
- Linked LIst
- Array
- Heap / Priority Queue
- HashMap
- Set

### Stack
- First-In Last-Out
- Good for items that have pairs (e.g. parentheses generation/validation)
- Good for problems that require having some kind of order
- Uses cases:
  - Managing function calls (call stack)
  - Undo/Redo functionality in text editors
  - Checking for balanced parentheses or valid expressions
  - Depth-First Search (DFS) implementation
  - Backtracking problems
- Common stack problems:
  - Valid Parentheses: Check if an expression has balanced parentheses.
  - Next Greater Element: Find the next greater element for each item in an array.
  - Daily Temperatures: Compute how many days you have to wait for a warmer temperature.
  - Min Stack: A stack that can retrieve the minimum element in O(1) time.
  - 
### Linked List
- A Linked List is a linear data structure where elements (nodes) are stored in memory non-contiguously and connected via pointers. Each node contains:
  - Value/Data
  - Pointer/Reference to the next node (for singly linked lists)
  - Optional: Pointer to the previous node (for doubly linked lists)
- Types of Linked Lists:
    - Singly Linked List (SLL) – Each node points to the next node.
    - Doubly Linked List (DLL) – Each node points to both next and previous nodes.
    - Circular Linked List (CLL) – The last node points back to the first node, forming a loop.
- Key Takeaways
  - ✅ Linked lists are useful when frequent insertions/deletions are needed.
  - ✅ Slow & fast pointers help detect cycles, find midpoints, etc.
  - ✅ Reversal problems typically require modifying pointers iteratively.
  - ✅ Dummy nodes simplify head operations and edge cases.
  
### Binary Tree
- Types of Binary Trees
  - Full Binary Tree – Every node has 0 or 2 children (no single-child nodes).
  - Complete Binary Tree – All levels are fully filled except possibly the last, which is filled from left to right.
  - Perfect Binary Tree – All levels are completely filled.
  - Balanced Binary Tree – Height difference between left and right subtrees is at most 1.
  - Degenerate (Skewed) Tree – Every node has only one child (becomes like a linked list).
 
### Binary Search Tree (BST)
- A Binary Search Tree (BST) is a sorted binary tree where:
  - The left subtree contains nodes with values less than the root.
  - The right subtree contains nodes with values greater than the root.
  - Each subtree follows the same BST property.
- Balanced BSTs (e.g., AVL, Red-Black Trees) guarantee O(log n) for search, insert, and delete.
- Unbalanced BSTs can degrade to O(n) in worst case (when the tree becomes a linked list).

### Heaps
- A Heap is a specialized binary tree that satisfies the heap property:
  - Max-Heap: The value of each node is greater than or equal to its children.
  - Min-Heap: The value of each node is less than or equal to its children.
- Heaps are typically implemented as binary trees stored in arrays.

- Heap Properties:
  - Complete Binary Tree:
    - All levels are fully filled except possibly the last, which is filled left to right.
  - Heap Property:
    - Max-Heap: Parent ≥ Children
    - Min-Heap: Parent ≤ Children
- Common Heap Problems:
  - Kth Largest Element:
    - Use a min-heap of size k.
  - Merge K Sorted Lists:
    - Use a min-heap for efficient merging.
  - Top K Frequent Elements:
    - Use a min-heap to maintain top k elements.
- Key Takeaways:
  - ✅ Heaps are efficient for priority-based tasks (O(log n) operations).
  - ✅ Commonly used in shortest path (Dijkstra's) and MST (Prim's) algorithms.
  - ✅ Efficient for problems involving frequent min/max extractions.
  - ✅ Heap sort has O(n log n) time complexity but is not stable.

## Algorithms/Tools
- Two Pointer
- Binary Search
- Topological Sort
- Backtracking
- Recursion

### Two-Pointer Technique
- Definition: A technique where two pointers traverse an array (or string) from different directions or at different speeds to solve a problem efficiently.
- Use Cases:
  - Finding pairs that meet a condition (e.g., two sum in a sorted array)
  - Removing duplicates in-place
  - Partitioning arrays
  - Reversing arrays or strings
  - Merging sorted arrays
-Types of Two-Pointer Approaches:
  - Opposite Ends (Left and Right Pointers)
    - Typically used for problems involving sorted arrays or palindromes.
    - One pointer starts at the beginning, and the other at the end.
    - Example: Finding a pair that sums to a target.
  - Same Direction (Slow and Fast Pointers)
    - One pointer moves slower than the other, commonly used for linked lists or removing duplicates.
    - Example: Detecting a cycle in a linked list.
- Time Complexity: Usually O(n), since each element is processed at most once.
- Opposite-end pointers are great for sorted input, while fast/slow pointers help in linked list cycle detection.


### Binary Search
- Algorithm that can search within a *sorted* list efficiently
- O(log(n)) where n is the length of the list
- Idea is to split the list in half, determine which of the two resulting lists would have the target, and continue to search within that list.

### Sliding Window

- The Sliding Window technique is an optimized approach used for problems involving contiguous subarrays or substrings. Instead of using a brute-force O(n²) approach, it dynamically expands and contracts a "window" over the input array/string, reducing time complexity to O(n) in many cases.
- Types of Sliding Window
  - Fixed-Length Window
    - The window size is pre-defined and moves in a linear fashion.
    - Example: Finding the maximum sum of k consecutive elements.
  - Variable-Length Window
    - The window expands and contracts dynamically based on conditions.
    - Example: Finding the smallest subarray with a sum >= target.


### Topological Sort

- Algorithm that traverses a graph and produces an order of the nodes in such a way that follows the order of dependencies
- Applicable problems include:
    - course scheduling (courses have prerequisites)
    - event scheduling
    - program dependencies (what dependencies must be built first in order for a program, *x*, to run
- only works with directed acyclic graphs
- How it works:
    1. start from a random node
    2. run DFS on its neighbors
    3. when you encounter a leaf-node, add to the resulting list in *reverse order*
        1. the order of adding to the list can vary depending on how the adjacency list is provided and/or if you flip the direction of the edges
    4. repeat steps 1-3 until you have visited all nodes
    5. return resulting list

### Backtracking

- Backtracking is an algorithm for finding all solutions by exploring all potential candidates
- If the solution candidate turns to be *not* a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, *i.e.* backtracks then tries again.
- Must output valid combinations. Stop exploring once a combination is not valid, in which case the combination “backtracks” to explore more combinations by removing elements in the current combination.
- Use cases:
  - combinations
  - permutations
  - subsets

### Recursion

- Can make code simpler and easier to understand. Allows a bigger problem to be solved by breaking the problem into smaller problems.

### 1D Dynammic Programming
- Dynamic Programming is a technique used to solve problems by breaking them down into overlapping subproblems and storing the results to avoid redundant calculations. 1D DP refers to problems where only a 1D array (or a single variable) is needed to store intermediate results.
- Key Concepts:
  - State Definition:
    - Define dp[i] to represent a meaningful subproblem.
    - Example: dp[i] could store the maximum profit at index i, the number of ways to reach index i, etc.
  - Transition Formula:
    - Find a recurrence relation to build the solution iteratively.
    - Example: dp[i] = dp[i-1] + dp[i-2] (Fibonacci sequence).
  - Base Case:
    - Identify initial values needed to start the DP process.
    - Example: dp[0] = 1, dp[1] = 1 for Fibonacci.
  - Optimization:
    - Sometimes, instead of storing an entire array, we can use only a few variables if the problem only requires the last few computed values.
    - Example: dp[i] only depends on dp[i-1] and dp[i-2], so we can use two variables instead of an array.
- Key Takeaways:
  - 1D DP often involves iterating over an array and updating a dp[i] state.
  - Space Optimization: If a problem only depends on the last 1-2 computed values, store only those instead of the entire DP array.
  - Common Patterns:
    - Subsequence problems → Compare previous elements (dp[i] = max/min(dp[i-1], …))
    - Counting problems → Sum the ways to reach dp[i]
    - Partitioning problems → Use dp[i] to track the best result up to i
  - Problems include: Fibonacci, Climbing Stairs, House Robber, Coin Change, Maximum Subarray (Kadane’s Algorithm), etc.
 
### Greedy Algorithm
- A Greedy Algorithm builds up a solution piece by piece, always choosing the locally optimal choice at each step with the hope that these choices lead to a globally optimal solution.
  - Does not reconsider previous choices (no backtracking).
  - Efficient but not always guaranteed to find the best solution for all problems.
- Key Characteristics of Greedy Algorithms:
  - Greedy Choice Property:
    - A global solution can be arrived at by selecting locally optimal choices.
  - Optimal Substructure:
    - An optimal solution to the problem contains optimal solutions to subproblems.
  - No Backtracking:
    - Once a choice is made, it is not revisited.
- When to Use Greedy Algorithms:
  - Problems with optimal substructure and greedy choice property.
  - Examples:
    - Huffman Coding (data compression).
    - Activity Selection (scheduling).
    - Dijkstra’s Algorithm (shortest path in non-negative weighted graphs).
    - Kruskal’s and Prim’s Algorithms (minimum spanning tree).
    - Coin Change Problem (only if coins are in a specific denomination).
- Key Takeaways:
  - ✅ Greedy algorithms are efficient but not always optimal.
  - ✅ Work best when problems have optimal substructure and greedy choice properties.
  - ✅ Fail for complex problems like 0/1 knapsack (use DP instead).
  - ✅ Efficient for MSTs, shortest paths in unweighted graphs, scheduling, etc.

## Quick Notes:
### General
- $$\frac{l + r}{2} = l + \frac{(r - l)}{2}$$ (when calculating mid-point for binary search, avoid overflow from calculating $${l+r}$$

### Python
- difference = list(set(A) - set(B))
- date.split('/') -> [01, 25, 2025]
- python doesn't have a built-in 'max'-heap, so use negatives values to emulate
- for w, v in zip(weights, values)
- for i, v in enumerate(some_list)
- .sort() sorts list in place
-   .sort(reverse=True) to sort in reverse
- intervals.sort(key=lambda x: x.start)
- Can access key-value pairs in dictionary with .items()
- tuples have value equality so you can compare tuples by value
- Can loop through array in reverse order with reversed(range(len(arr)) or range(len(arr)-1, -1, -1)
- "//" is floor division
- Can convert an array of primitives into a set with set(), e.g. numSet = set(nums)
- The ord() function returns the number representing the unicode code of a specified character
- Can swap values between variables in one line without 'tmp' variable (e.g. left, right = right, left)
- Python allows modifications to mutable objects (e.g. lists, dictionaries) from inner functions without requiring nonlocal
- deque is a double-ended queue
  - popleft()
  - append()
- some_list.copy() (or some_list[:] in python3) and copy = copy.deepcopy(some_list)
\
\
Collection of LeetCode questions to ace the coding interview! - Created using [LeetHub](https://github.com/QasimWani/LeetHub)

<!---LeetCode Topics Start-->
# LeetCode Topics
## Hash Table
|  |
| ------- |
| [0621-task-scheduler](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0621-task-scheduler) |
| [0768-partition-labels](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0768-partition-labels) |
## Two Pointers
|  |
| ------- |
| [0768-partition-labels](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0768-partition-labels) |
## String
|  |
| ------- |
| [0768-partition-labels](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0768-partition-labels) |
## Greedy
|  |
| ------- |
| [0621-task-scheduler](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0621-task-scheduler) |
| [0768-partition-labels](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0768-partition-labels) |

## Array
|  |
| ------- |
| [0621-task-scheduler](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0621-task-scheduler) |
## Sorting
|  |
| ------- |
| [0621-task-scheduler](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0621-task-scheduler) |
## Heap (Priority Queue)
|  |
| ------- |
| [0621-task-scheduler](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0621-task-scheduler) |
## Counting
|  |
| ------- |
| [0621-task-scheduler](https://github.com/vince-ermitano/leetcode_submissions/tree/master/0621-task-scheduler) |
<!---LeetCode Topics End-->
