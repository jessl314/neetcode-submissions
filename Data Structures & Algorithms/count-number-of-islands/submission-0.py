"""
the initial way that I am thinking of approaching this is dfs because we want a way to explore 
all the way to the end of an island. a potential issue noted for later I see is
that the island is not of some uniform rectangle shape so knowing if we are at the start of
an island or in the middle one can be difficult

my first thought would be to use a visited set to keep track of elements we have visited already


"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base check:
        if not grid:
            return 0
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # out of boundary check and check for a water cell or a cell we have seen
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return 

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # since an island could start from any cell we must do dfs starting
        # from each cell

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # seen start of island since r,c not in visited
                    count += 1
                    dfs(r, c)
        return count    