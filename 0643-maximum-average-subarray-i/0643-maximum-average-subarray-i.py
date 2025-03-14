class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # can calculate sum of k elements ending at some index, i,
        # in one pass
        # then just divide by k along the way
        # sliding window

        l = 0
        curr_sum = 0
        max_avg = float('-inf')

        for i in range(len(nums)):
            curr_sum += nums[i]

            if i - l + 1 == k:
                max_avg = max(max_avg, curr_sum / k)
                curr_sum -= nums[l]
                l += 1
        
        return max_avg
        

