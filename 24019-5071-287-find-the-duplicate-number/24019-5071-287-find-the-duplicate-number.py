class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            idx = abs(n)
            if nums[idx] < 0:
                return abs(n)
            nums[idx] *= -1