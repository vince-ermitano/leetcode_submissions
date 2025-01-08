class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()

        def backtrack(i, cur, sum):
            if sum == target:
                res.append(cur[:])
                return
            
            if sum > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            backtrack(i+1, cur, sum + candidates[i])
            cur.pop()

            while (i < len(candidates)-1 and candidates[i] == candidates[i+1]):
                i+=1

            backtrack(i+1, cur, sum)
        
        backtrack(0, [], 0)

        return res

