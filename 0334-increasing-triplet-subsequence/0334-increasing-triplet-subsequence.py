class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # instead of just checking each triplet in the array,
        # maintain the two of the smallest numbers nums[i], nums[j]
        # keeping them as small as possible until we find a nums[k] that meets
        # the increasing condition

        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            elif n > second:
                return True
        
        return False