class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1 = rob_2 = 0

        for n in nums:
            max_rob = max(rob_1 + n, rob_2)
            rob_1 = rob_2
            rob_2 = max_rob
        
        return rob_2