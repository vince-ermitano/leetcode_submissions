class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        initial_zeroes = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    initial_zeroes.add((i, j))


        def dfs(r, c, direction):
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS):
                return
            
            visited.add((r, c))
            matrix[r][c] = 0

            if (direction == 'row-left'):
                dfs(r, c - 1, direction)
            elif (direction == 'row-right'):
                dfs(r, c + 1, direction)
            elif (direction == 'col-up'):
                dfs(r - 1, c, direction)
            else:
                dfs(r + 1, c, direction)

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0 and (i, j) in initial_zeroes:
                    dfs(i - 1, j, 'col-up')
                    dfs(i + 1, j, 'col-down')
                    dfs(i, j - 1, 'row-left')
                    dfs(i, j + 1, 'row-right')


        