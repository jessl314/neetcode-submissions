"""
the initial way that I am thinking of approaching this is dfs because we want a way to explore 
all the way to the end of an island. a potential issue noted for later I see is
that the island is not of some uniform rectangle shape so knowing if we are at the start of
an island or in the middle one can be difficult

my first thought would be to use a visited set to keep track of elements we have visited already

this does work however it does end up using O(NxM) memory because at worst this visited set will hold nxm elements
and is O(nxm) due to the nested for loop

well after we encounter a 1 we technically don't need it anymore as long as we remember that location is part of an island
and we know that on first encounter from 0 to 1 that is the start of an island
so what if everytime we encounter a 1 we change it to 0 before dfs to all four directions
this way we know we won't mess up and consider that cell twice?


"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base check:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r, c):
            # out of boundary check and check for a water cell or a cell we have seen
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return 

            grid[r][c] = "0"


            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # since an island could start from any cell we must do dfs starting
        # from each cell

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
                    
        return count    