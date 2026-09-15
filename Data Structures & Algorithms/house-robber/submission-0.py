class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 tracks max profit up to 2 houses ago
        # rob2 tracks max profit up to 1 house ago
        rob1, rob2 = 0, 0
        
        # We iterate through each house
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            # We must choose the max between:
            # 1. Robbing this house (n) + max from two houses ago (rob1)
            # 2. Skipping this house and keeping max from one house ago (rob2)
            temp = max(n + rob1, rob2)
            
            # Now, shift our pointers forward for the next iteration
            rob1 = rob2
            rob2 = temp
            
        return rob2