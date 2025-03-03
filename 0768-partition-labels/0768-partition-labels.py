class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastInd = {}
        res = []

        for i, v in enumerate(s):
            lastInd[v] = i

        left = right = 0

        for i, v in enumerate(s):
            right = max(right, lastInd[v])

            if i == right:
                res.append(right - left + 1)
                left = right + 1
        
        return res
            


