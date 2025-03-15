class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # sliding window
        # if count of zeroes exceeds 1 in window
        # update left pointer until <= 1
        # keep track of length of window

        res = 0
        l = 0
        curr = 0
        zeroes_count = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes_count += 1
            
            while zeroes_count > 1:
                if nums[l] == 0:
                    zeroes_count -= 1
                
                l += 1
            
            res = max(res, r-l)

        return res