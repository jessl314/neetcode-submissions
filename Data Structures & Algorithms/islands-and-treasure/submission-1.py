class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        # 1. Start by finding ALL treasures (the sources)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        # 2. Run ONE BFS for the entire grid
        while q:
            r, c = q.popleft()
            
            for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                nr, nc = r + dr, c + dc
                
                # Boundary check + only move to unvisited empty rooms
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    # Update the distance in-place
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))