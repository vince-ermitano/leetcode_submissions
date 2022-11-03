class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        red = 0
        curr = 0
        blue = len(nums)-1
        
        while curr <= blue:
            
            if nums[curr] == 0:
                nums[curr], nums[red] = nums[red], nums[curr]
                red += 1
                curr += 1
            
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[blue] = nums[blue], nums[curr]
                blue -= 1