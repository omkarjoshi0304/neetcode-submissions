class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res , quad = [] , []

        def Ksum (start, k , target):

            if k != 2:
                for i in range(start ,  len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    Ksum(i + 1 , k - 1 , target - nums[i])
                    quad.pop()
                return

            
            l , r = start ,  len(nums) - 1

            while l < r:

                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        Ksum ( 0 , 4 , target)
        return res
            
