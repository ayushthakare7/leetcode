from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(board,r,c,rows,cols):
            if r<0 or c<0 or r>= rows or c>= cols:
                return
            # FIX 1: Stop traversing if the cell is an 'X'
            if visited[r][c]==1 or board[r][c] == "X":
                return
            visited[r][c]=1
            # FIX 2: Removed 'self.' because dfs is a nested function, not a class method
            dfs(board,r-1,c,rows,cols)
            dfs(board,r+1,c,rows,cols)
            dfs(board,r,c-1,rows,cols)
            dfs(board,r,c+1,rows,cols)

        r=0
        for c in range(cols):
            if board[r][c] == "O":
                dfs(board,r,c,rows,cols) # FIX 2
        c=0  
        for r in range(rows):
            if board[r][c] == "O":
                dfs(board,r,c,rows,cols) # FIX 2

        r=rows-1
        for c in range(cols):
            if board[r][c] == "O":
                dfs(board,r,c,rows,cols) # FIX 2

        c=cols-1
        for r in range(rows):
            if board[r][c] == "O":
                dfs(board,r,c,rows,cols) # FIX 2

        # FIX 3: Rewrote the final loop to correctly target unvisited 'O's and assign 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X" 
        
        # LeetCode expects in-place modification, so returning board is omitted.
