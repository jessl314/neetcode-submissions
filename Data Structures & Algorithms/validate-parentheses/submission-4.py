class Solution:
    def isValid(self, s: str) -> bool:
        """
        string -> these types of characters only 
        a valid string is if the brackets balanced

        (()())
        
        
        """
        brackets = {")":"(", "}":"{", "]":"["}

        stack = []

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif stack and stack[-1] == brackets[c]:
                stack.pop()
            else:
                return False

        if stack:
            return False
        return True
        