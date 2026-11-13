class MinStack:
    """
    stack: LIFO

    we need a real stack -> list but also something that will always return min element
    ok for minimum we could also do stack? but for this one it is like every time we encounter a new value we compare to last element in min stack and add the min val at that time? that way min val is always on top. 


    
    
    """

    def __init__(self):
        self.stack = []
        self.minstack = []

        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # new value is currently minimum of stack
        if not self.minstack:
            self.minstack.append(val)
        else:
            # append minimum to top of stack
            self.minstack.append(min(val, self.minstack[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]
    
        
