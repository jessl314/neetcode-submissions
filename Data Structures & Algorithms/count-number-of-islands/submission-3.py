class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        def dfs(r, c):
            # no search if point is out of boundaries or 
            # it is not an unvisited island point
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            # visit it
            grid[r][c] = "0"

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                dfs(nr, nc)

        # since an island could start from any cell we must do dfs starting
        # from each cell

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
                    
        return count    