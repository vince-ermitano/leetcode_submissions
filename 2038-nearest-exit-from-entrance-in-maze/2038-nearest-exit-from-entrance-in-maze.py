class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs from the entrance
        # once we hit an exit that isn't the entrance, return the 'level' that we're at
        # if our bfs q becomes empty and haven't reached an exit, return -1

        q = deque()
        level = 0
        visited = set()
        ROWS = len(maze)
        COLS = len(maze[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q.append(tuple(entrance))

        while q:

            for i in range(len(q)):
                row, col = q.popleft()

                # skip if wall, out of bounds, or visited
                if (row < 0 or row >= ROWS or 
                col < 0 or col >= COLS or
                maze[row][col] == '+' or
                (row, col) in visited):
                    continue
                
                visited.add((row, col))

                # explore other directions
                for dr, dc in directions:
                    q.append((row + dr, col + dc))

                # return when we reach an exit
                if not (row == entrance[0] and col == entrance[1]) and (row == 0 or row == ROWS-1 or col == 0 or col == COLS-1):
                    return level
                
            level += 1
        
        return -1