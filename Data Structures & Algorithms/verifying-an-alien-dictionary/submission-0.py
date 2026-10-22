class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. Map each alien character to its priority index
        alien_order = {char: index for index, char in enumerate(order)}
        
        # 2. Check every adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            # 3. Compare characters one by one
            for j in range(len(w1)):
                # Edge Case: w1 is longer than w2, but they matched perfectly so far
                # (e.g., w1="apple", w2="app" -> Should be False)
                if j == len(w2):
                    return False
                
                # If characters differ, evaluate their alien priority
                if w1[j] != w2[j]:
                    if alien_order[w1[j]] > alien_order[w2[j]]:
                        return False
                    
                    # If w1's character is strictly smaller, this pair is valid.
                    # Break the inner loop to move to the next pair of words.
                    break
                    
        return True