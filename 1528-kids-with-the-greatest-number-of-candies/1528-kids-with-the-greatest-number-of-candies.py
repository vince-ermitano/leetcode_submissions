class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandiesInitial = max(candies)
        res = [False] * len(candies)

        for i in range(len(candies)):
            if extraCandies + candies[i] >= mostCandiesInitial:
                res[i] = True
        
        return res