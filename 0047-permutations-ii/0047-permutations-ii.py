class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        chosen = [False for i in range(len(nums))]
        res = []


        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if chosen[i]: continue
                if i > 0 and nums[i-1] == nums[i] and not chosen[i-1]: continue
                
                curr.append(nums[i])
                chosen[i] = True
                backtrack(curr)
                curr.pop()
                chosen[i] = False
        
        backtrack([])
        return res