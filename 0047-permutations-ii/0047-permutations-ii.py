class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        res = []

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for k, v in counts.items():
                if v > 0:
                    curr.append(k)
                    counts[k] -= 1
                    backtrack(curr)
                    curr.pop()
                    counts[k] += 1

        backtrack([])        

        return res