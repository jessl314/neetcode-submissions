"""
the initial way that I am thinking of approaching this is dfs because we want a way to explore 
all the way to the end of an island. a potential issue noted for later I see is
that the island is not of some uniform rectangle shape so knowing if we are at the start of
an island or in the middle one can be difficult

my first thought would be to use a visited set to keep track of elements we have visited already

this does work however it does end up using O(NxM) memory because at worst this visited set will hold nxm elements
and is O(nxm) due to the nested for loop

if we want to reduce chance of stack recursive overflow then I could also consider a bfs approach


"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # base check:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        count = 0
        
        def bfs(r, c):
            # out of boundary check and check for a water cell or a cell we have seen

            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
                    


        # since an island could start from any cell we must do dfs starting
        # from each cell

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
                    
        return count    