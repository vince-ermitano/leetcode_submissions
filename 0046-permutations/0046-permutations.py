class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        n = len(nums)
        
        def backtrack(first):
            if first == n:
                permutations.append(list(nums))
            for i in range(first, n):
                temp = nums[first]
                nums[first] = nums[i]
                nums[i] = temp
                
                backtrack(first+1)
                
                temp = nums[first]
                nums[first] = nums[i]
                nums[i] = temp
        
        backtrack(0)
        return permutations
                
        