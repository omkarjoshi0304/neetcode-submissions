class TrieNode:
    def __init__(self):
        self.child = {}
        self.endofword = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.endofword = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.endofword
            
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return True

        
        