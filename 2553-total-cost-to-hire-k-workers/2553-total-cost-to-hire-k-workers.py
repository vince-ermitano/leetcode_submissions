class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Maintain two minheaps handling the candidates from the front
        # of the list and from the back
        # Compare the min from each heap and hire the one with the cheapest
        # cost until we hire k workers

        i, j = 0, len(costs)-1
        h1, h2 = [], []
        total = 0

        while k > 0:
            # build h1
            while len(h1) < candidates and i <= j:
                heapq.heappush(h1, costs[i])
                i += 1
            # build h2
            while len(h2) < candidates and i <= j:
                heapq.heappush(h2, costs[j])
                j -= 1

            cost_1 = h1[0] if h1 else float('inf')
            cost_2 = h2[0] if h2 else float('inf')

            if cost_1 <= cost_2:
                total += heapq.heappop(h1)
            else:
                total += heapq.heappop(h2)

            k -= 1
        
        return total