class MyQueue:

    def __init__(self):
        # self.queue = []
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # self.queue.append(x)
        self.stack1.append(x)

    def pop(self) -> int:
        # if len(self.queue) != 0: return -1
        # else: return self.queue.pop(0)

        if len(self.stack2) == 0: 
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        # if len(self.queue) == 0: return -1
        # else: 
        #     return self.queue[0]
        if len(self.stack2) == 0: 
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # if len(self.queue) == 0: return True
        # else: return False
        if len(self.stack1) == 0 and len(self.stack2) == 0: return True
        else: return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()