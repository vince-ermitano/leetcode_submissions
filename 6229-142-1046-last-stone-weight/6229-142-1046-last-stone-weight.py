class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [(x * -1) for x in stones]
        heapq.heapify(stones)

        while (len(stones) > 1):
            stone1 = abs(heapq.heappop(stones))
            stone2 = abs(heapq.heappop(stones))

            remains = abs(stone1 - stone2)

            if remains > 0:
                heapq.heappush(stones, remains * -1)
            
        return stones[0] * -1 if len(stones) > 0 else 0
        