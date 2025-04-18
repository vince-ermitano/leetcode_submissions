class StockSpanner:
    # maintain a monotonic stack that pushes each price and res (spans)
    # when we encounter a price that is larger than the top of the stack,
    # we keep incrementing res and popping from the stack until this is not the case, in which we
    # will push (price, res) to the stack.
    # This means that when there is any price that is still in the stack, we have not seen a larger
    # price afterwards and thus no price we have seen can expand on that res.

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        res = 1

        # calculate span for current day
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1] # add onto the span of the lower priced day
        
        self.stack.append((price, res))

        return res

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)