class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or prevHeight > heights[r][c]):
                return

            visited.add((r, c))
            for dr, dc in directions:
                new_r = dr + r
                new_c = dc + c
                dfs(new_r, new_c, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        
        return res
        