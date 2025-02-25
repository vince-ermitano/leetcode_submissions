class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        if not height: return res

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while (l < r):
            if leftMax < rightMax:
                l += 1
                trapped = min(leftMax, rightMax) - height[l]

                if trapped > 0:
                    res += trapped
                
                leftMax = max(leftMax, height[l])

            else:
                r -= 1
                trapped = min(leftMax, rightMax) - height[r]

                if trapped > 0:
                    res += trapped

                rightMax = max(rightMax, height[r])
        return res