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

## Algorithms

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

\
\
Collection of LeetCode questions to ace the coding interview! - Created using [LeetHub](https://github.com/QasimWani/LeetHub)
