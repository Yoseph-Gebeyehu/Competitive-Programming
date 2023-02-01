class MyQueue:

    def __init__(self):
        self.myQueue=[]
        

    def push(self, x: int) -> None:
        return self.myQueue.append(x)
        

    def pop(self) -> int:
        return self.myQueue.pop(0)
        

    def peek(self) -> int:
        return self.myQueue[0]
        

    def empty(self) -> bool:
        return len(self.myQueue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
