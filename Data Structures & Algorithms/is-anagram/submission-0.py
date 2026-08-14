class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_count = {}

        for char in s:
            my_count[char] = my_count.get(char, 0) + 1
        
        for char in t:
            if char not in my_count or my_count[char] == 0:
                return False

            my_count[char] -= 1
        
        return True

