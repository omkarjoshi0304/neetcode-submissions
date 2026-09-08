class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row , col = len(board) , len(board[0])

        def dfs(r , c):
            if (r < 0 or c < 0 or c >= col or r >= row or board[r][c] != "O" ):
                return
            
            board[r][c] = "T"

            dfs(r + 1 , c)
            dfs(r - 1, c)
            dfs(r , c + 1)
            dfs(r , c - 1)

        
        for c in range(col):
            dfs(0 , c)
            dfs( row - 1 , c)
        
        for r in range(row):
            dfs(r , 0)
            dfs(r , col - 1)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O" 

