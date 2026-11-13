class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        understanding: an island is represented by some cluster of 1's (one or more cells) such that it is surrounded by zeros in the horizontal/vertical direction. 
        primary concern: how do we know that we have not counted redundantly. we can do this by having a structure to store visited cells -> the one we currently process and any neighbor that is a 1 that is also not in visited yet (which we add to the next to be processed structure) -> basically adding potential new islands to process next. until there are no more 1s the island count stays the same 

        given that I want to track visited cells this leans the most towards using a graph type structure with some search algorithm, like BFS or DFS. 

        since the problem statement uses the word "adjacent" I feel it is more intuitive to use BFS

        verbal algo walk through..... uh oh my initial issue 

        was in this case 0 1 1 if we move to the second 1 then only one neighbour is visited so now this new 1 may be counted as another island so, the change is that only after the nodes currently in queue have all been processed (so all 1's in a particular island marked visited) do we move our search to the next cell.

        visited is set because we don't want duplicated visited cells 

        for each cell if it is a potential new island (a 1) and we have not visited it yet we search to expand our island and increment number of islands only once for this entire search (thus eliminating multiple counting islands)


        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()
        count = 0

        def bfs(r, c):
            """ queue is the data structure to hold 
            all nodes to be processed for a particular island """
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    count += 1
        return count
