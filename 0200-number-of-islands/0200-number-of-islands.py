class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_of_islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                else:
                    self.dfs(grid, i, j)
                    num_of_islands+=1
        
        return num_of_islands
    
    def dfs(self, grid, row, col):
        if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0'):
            return
        else:
            grid[row][col] = '0'
            self.dfs(grid, row-1, col)
            self.dfs(grid, row+1, col)
            self.dfs(grid, row, col-1)
            self.dfs(grid, row, col+1)
        