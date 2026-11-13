class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position array: positions, speed array: speeds -> all integer arrays

        p = [1, 4], speed = [3, 2] target = 10
        time_to_reach = (target - position) / speed

        0th hour
        [4, 6] -> [7, 8] -> [8, 8] -> destination

        essentially each car can only be compared with the most recently added car in front of it
        ok then so we should pair these speeds and positions together then sort by position
        but the ones closer 

        (4, 2), (1, 3)
        time = 3
        ok so any car that can reach dest faster will "pass" the one in the stack so we can pop. then at the end count number of fleets

        what if we used a stack then for LIFO

        [(4, 2)] (1, 3) has a time of 3 too
        so we pop and append [(1,3)] we have one fleet but no more cars to consider so 
        return 1

        stack = []

        for i in range(len(pairs)):
            cars.append((pairs[i], speed[i]))
        
        cars.sort(reverse=True)

        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack >= 2) and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        """
        stack = []
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)