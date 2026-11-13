class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        count = 0
        def bfs(r, c):
            # establish nodes to process
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc)) 

        # since an island could start from any cell we must do dfs starting
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
                    
        return count    