# Sort points by x_end
# Traverse through points maintaining the highest x_start and lowest x_end seen
# If a point is not between those constraints, we know that we need to throw a
# new arrow to pop the current balloon.
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by x_end
        points.sort(key=lambda x: x[1])

        arrows = 1
        left, right = points[0][0], points[0][1]

        for x_start, x_end in points:
            if x_start > right:
                arrows += 1
                left, right = x_start, x_end
            else:
                left = max(left, x_start)
                right = min(right, x_end)
        
        return arrows
        
