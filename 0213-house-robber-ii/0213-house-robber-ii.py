class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Idea is to run emulate robbing from house_1 to house_n-1 and then from house_2 to house_n
        # since we can't rob house_1 and house_n. Catch edge case where there is only one house to rob
        
        # rob house along a straight-line street (i.e. house robber I)
        def helper(nums):
            rob_1 = rob_2 = 0

            for n in nums:
                max_rob = max(n + rob_1, rob_2)
                rob_1 = rob_2
                rob_2 = max_rob

            return rob_2

        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))