class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        so it is basically saying that result[i] is the number of indices after i where
        temp[j] > temp[i]

        first thought: for each element iterate through remaining elements to find an element larger than the fixed element
        results = [0] * len(temperatures)
        for i in range(temperatures):
            count = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
        
        [30,38,30,36,35,40,28]
        []

        this ends up being O(n^2)
        hm but what if instead of manually checking all elements in the list we
        keep a structure for only the temps that need to find a larger future temp

        [30,38,30,36,35,40,28]

        [40,28]
        [1,4,1,2,1,0,0]

        stack = [(temperatures[0], 0])]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((temperatures[i], i))
        return res
        """
        stack = [(temperatures[0], 0)]
        result = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((temperatures[i], i))
        return result
        