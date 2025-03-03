class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        chosen = [False for i in range(len(nums))]
        res = []

        duplicates = set()

        def backtrack(curr, chosen):
            if len(curr) == len(nums):
                curr_tuple = tuple(curr)

                if curr_tuple in duplicates: return

                res.append(curr[:])
                duplicates.add(curr_tuple)
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