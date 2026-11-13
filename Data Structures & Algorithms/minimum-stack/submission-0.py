class MinStack:
    """
    initial thoughts: minheap since we want minimum element but this doesn't really work 
    because we have pop and top which require original order of elements


    
    
    """

    def __init__(self):
        self.stack = []
        self.minstack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
        
