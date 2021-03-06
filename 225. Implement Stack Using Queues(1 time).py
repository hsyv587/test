class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.pop())

        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        res = self.queue[0]
        del self.queue[0]
        return res       

    def top(self):
        """
        Get the top element.
        :rtype: int
        """   
        return self.queue[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.queue:
            return False
        return True

        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()