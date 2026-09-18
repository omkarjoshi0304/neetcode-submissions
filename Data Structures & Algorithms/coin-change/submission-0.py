class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Initialize the DP array. 
        # (amount + 1) acts as our "infinity" because you can never use 
        # more coins than the amount itself (even if coins were all 1s).
        dp = [amount + 1] * (amount + 1)
        
        # 2. Base case: 0 coins needed to make amount 0
        dp[0] = 0
        
        # 3. Calculate the minimum coins for every amount from 1 up to the target
        for a in range(1, amount + 1):
            for c in coins:
                # If the coin is small enough to fit in the current amount
                if a - c >= 0:
                    # Update our best count using the recurrence relation
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    
        # 4. If the final answer is still our fake "infinity", it means it's impossible
        return dp[amount] if dp[amount] != amount + 1 else -1