import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                val = board[r][c]

                if (val in rows[r] or 
                    val in col[c] or 
                    val in square[(r // 3 , c //3)]):
                    return False

                rows[r].add(val)
                col[c].add(val)
                square[(r//3 ,c//3)].add(val)
        return True