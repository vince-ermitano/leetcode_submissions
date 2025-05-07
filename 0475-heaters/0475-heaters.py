class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Approach:
        # Sort heaters
        # For every house, use binary search to find the nearest heater
        # Find the max distance of the nearest heaters for each house to find the minimum radius

        heaters.sort()
        radius = 0

        for house in houses:
            left, right = 0, len(heaters)-1

            # find nearest heater to right of house
            while left < right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
                
            dist = abs(heaters[left] - house)

            if left > 0:
                dist = min(dist, abs(heaters[left-1]-house))
            radius = max(radius, dist)

        return radius
