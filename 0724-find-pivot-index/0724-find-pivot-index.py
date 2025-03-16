class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # set prefix sum to 0 and postfix sum to sum(nums)
        # iterate through nums and substract curr element from postfix sum
        # then check if prefix and postfix are equal
        # then add curr element to prefix sum
        
        prefix, postfix = 0, sum(nums)

        for i in range(len(nums)):
            postfix -= nums[i]

            if prefix == postfix:
                return i
            
            prefix += nums[i]
        
        return -1

