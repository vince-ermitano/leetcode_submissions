class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ans = []
        left = 0
        right = len(numbers) - 1
        
        while (True):
            if (numbers[left] + numbers[right] == target):
                ans.append(left+1)
                ans.append(right+1)
                break;
            
            elif (numbers[left] + numbers[right] < target):
                left+=1
            else:
                right-=1
        
        return ans
        