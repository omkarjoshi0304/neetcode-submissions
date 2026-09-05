class TrieNode:
    def __init__(self):
        self.child = {}
        self.isWord = False
    def addword (self , word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isWord = True
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)
        row , col = len(board) , len(board[0])
        res , visit = set() , set()

        def dfs(r , c , node , word ):
            if (r < 0 or c < 0 or r == row or c == col or board[r][c] not in node.child or (r , c) in visit ):
                return
            
            visit.add((r , c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            dfs(r + 1 , c , node , word)
            dfs(r - 1 , c, node , word)
            dfs(r , c + 1 , node , word)
            dfs(r , c - 1 , node , word)

            visit.remove((r , c))
        for r in range(row):
            for c in range(col):
                dfs (r , c , root , "")
        return list(res)

