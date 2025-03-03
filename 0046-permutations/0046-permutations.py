class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        chosen = [False for i in range(len(nums))]

        print(chosen)

        def backtrack(curr, chosen):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if not chosen[i]:
                    curr.append(nums[i])
                    chosen[i] = True
                    backtrack(curr, chosen)

                    curr.pop()
                    chosen[i] = False
        
        backtrack([], chosen)

        return res
        