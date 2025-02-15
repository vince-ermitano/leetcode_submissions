class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_fresh = 0
        minutes = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while num_fresh and q:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if (0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1):
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 2
                        num_fresh -= 1
            
            minutes += 1
        
        return minutes if num_fresh == 0 else -1

                
