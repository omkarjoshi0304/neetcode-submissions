class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0
        for n in nums:

            if (n - 1) not in num_set:
                curr_long = 1

                while (n + curr_long) in num_set:
                    curr_long += 1

                longest = max(longest , curr_long)
        return longest

        