class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        ROWS, COLS = len(board), len(board[0])

        def backtrack(r, c, i):
            if (i == len(word)):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
                or board[r][c] != word[i] or board[r][c] == '!'):
                return False

            board[r][c] = '!'
            res = (backtrack(r+1, c, i+1)
                or backtrack(r-1, c, i+1)
                or backtrack(r, c+1, i+1)
                or backtrack(r, c-1, i+1))
            
            board[r][c] = word[i]
            return res
        
        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if (backtrack(r, c, 0)):
                    return True

        return False
        