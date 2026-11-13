class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        INF = 2147483647
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # on cells with INf value
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or visited[r][c]:
                return INF
            # we have found a treasure chest instead of a INF
            if grid[r][c] == 0:
                return 0

            visited[r][c] = True
            result = INF
            for dr, dc in directions:
                result = min(result, 1 + dfs(r + dr, c + dc))
            # this cell could still be part of another distance calculation
            visited[r][c] = False
            return result
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)

            
            