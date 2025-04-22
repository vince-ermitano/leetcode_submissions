# Sort points by x_end
# Traverse through points maintaining the x_end of the balloon that we start throwing an arrow with.
# If a point's x_start is not less than this constraint, we know that we need to throw a
# new arrow to pop the current balloon and update the right constraint
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by x_end
        points.sort(key=lambda x: x[1])

        arrows = 1
        right = points[0][1]

        for x_start, x_end in points:
            # throw a new arrow when the curr balloon cannot be popped by the curr arrow
            if x_start > right:
                arrows += 1
                right = x_end
        
        return arrows
        
