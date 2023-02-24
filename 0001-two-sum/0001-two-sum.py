class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        
        for i in range(len(nums)):
            print(nums[i])
            if (target - nums[i]) in seen.keys():
                print(seen)
                ans.append(seen[target-nums[i]])
                ans.append(i)
                break
            
            seen[nums[i]] = i
        
        return ans
        