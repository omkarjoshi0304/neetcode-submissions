class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       maps = {}

       for i , num in enumerate(nums):

        complement = target - num

        if complement in maps:
            return [maps[complement] , i]
        
        maps[num] = i



