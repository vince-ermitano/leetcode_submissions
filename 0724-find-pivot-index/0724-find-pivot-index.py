class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # compute prefix sums and postfix sums for each index
        # loop through nums and check if prefix and postfix computations
        # at specific index are the same

        prefix = []
        postfix = []

        curr = 0

        for n in nums:
            prefix.append(curr)
            curr += n

        curr = 0

        for n in reversed(nums):
            postfix.insert(0, curr)
            curr += n
            
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        
        return -1
        

