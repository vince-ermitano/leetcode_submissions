class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        def backtrack(i, cur):
            if i >= len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            backtrack(i+1, cur)

            cur.pop()

            while (i + 1 < len(nums) and nums[i+1] == nums[i]):
                i += 1

            backtrack(i+1, cur)

        backtrack(0, [])
        return res
        