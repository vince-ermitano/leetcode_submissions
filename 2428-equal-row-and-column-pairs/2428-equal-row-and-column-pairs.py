class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # create a hashmap with k,v pairs where
        # k is the tuple of a rows elements
        # v is the count of k's occurences
        # iterate through the grid's columns
        # and if that column's sequence of elements
        # is in our hashmap, increment result by how
        # many times it appears in the grid's rows
        
        n = len(grid)
        row_map = defaultdict(int)

        for arr in grid:
            row_map[tuple(arr)] += 1

        pairs = 0

        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            pairs += row_map[column]

        return pairs

