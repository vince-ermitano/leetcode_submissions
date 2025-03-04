class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr):

            if len(curr) == k:
                res.append(curr[:])
                return
            if i == n+1:
                return

            for j in range(i, n + 1):
                curr.append(j)
                backtrack(j+1, curr)
                curr.pop()
        
        backtrack(1, [])
        return res