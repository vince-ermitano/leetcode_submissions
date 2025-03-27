class SmallestInfiniteSet:

    # have a minHeap initialized with just a '1' in it
    # when we popSmallest, pop from the minHeap and also add the next number
    # that should be in the heap (keep track with a 'last added' variable)
    # Just push to heap in addBack
    # keep track of whats in the set by keeping track of what has gotten removed and added back

    def __init__(self):
        self.heap = [1]
        self.lastAdded = 1
        self.removed = set()
        heapq.heapify(self.heap)

        

    def popSmallest(self) -> int:
        self.lastAdded += 1
        heapq.heappush(self.heap, self.lastAdded)
        popped = heapq.heappop(self.heap)
        self.removed.add(popped)
        return popped

    # push num to heap if in 'removed' set
    def addBack(self, num: int) -> None:
        if num in self.removed:
            heapq.heappush(self.heap, num)
            self.removed.remove(num)

        return
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)