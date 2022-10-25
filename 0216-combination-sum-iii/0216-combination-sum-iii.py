class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        
        def backtrack(remaining_sum, curr_comb, next_start):
            if remaining_sum == 0 and len(curr_comb) == k:
                ans.append(list(curr_comb))
                return
            elif remaining_sum < 0 or len(curr_comb) == k:
                return
            
            for i in range(next_start, 10):
                curr_comb.append(i)
                backtrack(remaining_sum - i, curr_comb, i + 1)
                curr_comb.pop()
                
        
        backtrack(n, [], 1)
        
        return ans
        