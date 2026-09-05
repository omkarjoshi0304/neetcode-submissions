class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posdig = set()
        negdig = set()
        col = set()

        res = []
        board = [["."] * n for i in range(n)]

        def dfs(r):
            if  r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r + c) in posdig or (r - c) in negdig:
                    continue
                col.add(c)
                posdig.add(r + c)
                negdig.add(r - c)
                board[r][c] = "Q"

                dfs(r + 1)

                col.remove(c)
                posdig.remove(r + c)
                negdig.remove(r - c)
                board[r][c] = "."
        dfs(0)
        return res

