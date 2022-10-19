class MinStack(object):

    def __init__(self):
        self.norm_list = []
        self.min_list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.norm_list.append(val)
        
        if (not self.min_list or val <= self.min_list[-1]):
            self.min_list.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        popped = self.norm_list.pop()
        
        if (popped == self.min_list[-1]):
            self.min_list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.norm_list[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()