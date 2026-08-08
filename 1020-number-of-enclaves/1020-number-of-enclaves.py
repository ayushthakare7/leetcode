from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, rows, cols, grid):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if visited[r][c] == 1 or grid[r][c] == 0:
                return
            visited[r][c] = 1
            grid[r][c] = 0
            dfs(r-1, c, rows, cols, grid)
            dfs(r+1, c, rows, cols, grid)
            dfs(r, c-1, rows, cols, grid)
            dfs(r, c+1, rows, cols, grid)

        # 1. Top Row boundary
        for c in range(cols):
            dfs(0, c, rows, cols, grid)

        # 2. Left Column boundary
        for r in range(rows):
            dfs(r, 0, rows, cols, grid)

        # 3. Bottom Row boundary (FIXED: rows - 1)
        for c in range(cols):
            dfs(rows - 1, c, rows, cols, grid)

        # 4. Right Column boundary (FIXED: cols - 1)
        for r in range(rows):
            dfs(r, cols - 1, rows, cols, grid)

        # 5. Count remaining unvisited land cells
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
        return count
