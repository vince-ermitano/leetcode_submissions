class SmallestInfiniteSet:

    # have a minHeap initialized with just a '1' in it
    # when we popSmallest, pop from the minHeap and also add the next number in the sequence
    # of the infinite set (keep track with a 'last added' variable)
    # keep track of whats in our q by keeping track of what has gotten removed and added back
    # addBack will add the number back in our queue if the number has been removed

    def __init__(self):
        self.heap = [1]
        self.lastAdded = 1 # keep track of the next number in the sequence
        self.removed = set() # keep track of what has been removed
        heapq.heapify(self.heap)

    # add the next number in the sequence to the heap
    # pop and add the min value from the heap to our 'removed' list
    # return the value
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