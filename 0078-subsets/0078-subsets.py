class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)
            
        backtrack(0, [])
        return res