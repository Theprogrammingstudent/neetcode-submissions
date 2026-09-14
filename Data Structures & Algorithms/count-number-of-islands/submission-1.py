class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #check if the grid is empty
        if not grid:
            return 0

        #set vars
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0

        #BFS traversal
        def bfs(r, c):
            # Declare Q, add coords to visit and Q
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            
            while q:
                #popleft = BFS .pop = DFS
                row, col = q.popleft()
                #left, right, up, down
                directions = [[1,0],[-1,0], [0,1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        # check every square - if grid[r][c] == "1" and (r,c) not in visit
        # start BFS
        # Add a new island
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands

