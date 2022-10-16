class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_products = [None] * len(nums)
        right_products = [None] * len(nums)
        answer = [None] * len(nums)
        
        curr_product = 1
        
        for i in range(len(nums)):
            left_products[i] = nums[i] * curr_product
            curr_product = left_products[i]
            
        curr_product = 1
        
        for i in reversed(range(len(nums))):
            right_products[i] = nums[i] * curr_product
            curr_product = right_products[i]
            
        for i in range(len(nums)):
            if (i-1 < 0):
                answer[i] = right_products[i+1]
                continue
            if (i+1 >= len(nums)):
                answer[i] = left_products[i-1]
                continue
            
            answer[i] = left_products[i-1] * right_products[i+1]
            
        return answer
            
            
        