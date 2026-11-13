class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        so the idea is we see number number operation
        perform operation to get a new number then continue number operation is on
        this current number and the new number -> operation is always performed on
        the two most recent seen or calculated numbers -> stack

        -> the issue is with communitive proproperty so since stack lifo. if we do 
        subtraction we need to reverse the order in which operate

        [1 2 + 3 * 4 -]
        [9 4] -> 9 - 4 = 5

        op_stack = []
        result = 0

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                op_stack.append(int(token))
            else:
                first, second = op_stack.pop(), op_stack.pop()
                if token == "+":
                    result = second + first
                    
                elif token == "-":
                    result = second - first
                elif token == "*":
                    result = second * first
                else:
                    result = int(second / first)
                op_stack.append(result)
        return op_stack[0]       
        """
        op_stack = []
        result = 0

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                op_stack.append(int(token))
            else:
                first, second = op_stack.pop(), op_stack.pop()
                if token == "+":
                    result = second + first
                    
                elif token == "-":
                    result = second - first
                elif token == "*":
                    result = second * first
                else:
                    result = int(second / first)
                op_stack.append(result)
        return op_stack[0]       
        