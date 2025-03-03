class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        time = 0
        maxHeap = [-x for x in counts.values()]
        heapq.heapify(maxHeap)
        q = deque() # store [counts, timeAvailable]

        while maxHeap or q:
            time += 1

            if maxHeap:
                remainingCopies = 1 + heapq.heappop(maxHeap)

                if remainingCopies:
                    q.append([remainingCopies, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
        

