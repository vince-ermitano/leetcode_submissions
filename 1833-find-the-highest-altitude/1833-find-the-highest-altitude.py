class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # compute current altitude by adding net gain
        # keep track of max altitude after each calculation

        largest = 0
        curr = 0

        for n in gain:
            curr += n
            largest = max(largest, curr)

        return largest