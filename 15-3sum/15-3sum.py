class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if (nums[i] > 0):
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                self.twoSum(nums, i, ans)
        
        return ans
    
    def twoSum(self, nums, current_ind, ans):
        
        low = current_ind + 1
        high = len(nums) - 1
        
        while (low < high):
            curr_sum = nums[current_ind] + nums[low] + nums[high]
            if (curr_sum < 0):
                low+=1
            elif (curr_sum > 0):
                high-=1
            else:
                
                ans.append([nums[current_ind], nums[low], nums[high]])
                low += 1
                high -= 1

                while (low < high) and (nums[low] == nums[low-1]):
                    low += 1
        