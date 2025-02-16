class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or board[r][c] != "O"):
                return
            board[r][c] = "N"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and r in [0, ROWS-1] or c in [0, COLS-1]):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"
        return
        