class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def backtrack(target, curr_combination, start_index):
            if (target == 0):
                ans.append(list(curr_combination))
                
            elif (target < 0):
                return
            
            for i in range(start_index, len(candidates)):
                curr_combination.append(candidates[i])
                backtrack(target - candidates[i], curr_combination, i)
                curr_combination.pop()
                
        backtrack(target, [], 0)
        return ans
        