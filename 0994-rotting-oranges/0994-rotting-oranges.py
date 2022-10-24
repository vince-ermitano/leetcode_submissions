class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
    
        num_fresh_oranges = 0
            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh_oranges += 1
            
        if (len(queue) == 0):
            if num_fresh_oranges != 0:
                return -1
            return 0
            
        min_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            
            min_elapsed += 1
            
            len_of_queue = len(queue)
                
            for i in range(len_of_queue):
                row, col = queue.popleft()
            

                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                        
                    if len(grid) > neighbor_row >= 0 and len(grid[0]) > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            
                            grid[neighbor_row][neighbor_col] = 2
                            num_fresh_oranges -= 1
                            queue.append((neighbor_row, neighbor_col))
                            
        return min_elapsed if num_fresh_oranges == 0 else -1
                            
                
                
        # IDEA
        # * Utilize BFS
        # * First traverse through the grid and find the rotten tomatoes and the number of fresh tomatoes
        # * while the queue of rotten tomatoes is not empty, explore it's neighbors and contaminate if needed
        #     (make sure to keep track of each minute cycle)
        # * once this queue is empty that means the rotten tomatoes can no longer contaminate so we just need to
        #     check if all the fresh tomatoes have been contaminated. If yes, return the minutes elapsed. Else return -1
            