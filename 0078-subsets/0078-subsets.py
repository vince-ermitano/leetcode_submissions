class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        subset = []
        
        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)
            
        
        backtrack(0)
        
        return res
        