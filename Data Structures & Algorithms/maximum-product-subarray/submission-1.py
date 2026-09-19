class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curmax , curmin = 1 ,1 

        for n in nums:
            if n == 0:
                curmax = curmin = 1
                continue
            
            tmp = curmax * n
            curmax = max(n * curmax , n * curmin ,  n)
            curmin = min(tmp , n * curmin , n )
            res = max(res , curmax)
        return res