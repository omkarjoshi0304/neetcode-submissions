class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs( i , cur_sum):
            if (i , cur_sum) in dp:
                return dp[(i , cur_sum)]

            if i == len(nums):
                return 1 if cur_sum == target else 0
            dp[(i , cur_sum)] = (dfs ( i + 1, cur_sum + nums[i]) + dfs (i + 1 , cur_sum - nums[i]))

            return dp[(i , cur_sum)]
        
        return dfs(0 , 0)