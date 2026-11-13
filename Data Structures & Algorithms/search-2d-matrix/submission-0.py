class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        so first -> valid input, all integers
        is it saying that essentially both rows and columns are in non-decreasing order (ex:
        2nd row first element greater than first row last element etc...)

        first thought -> O(n^2) is of course search through every element
        O(log(m*n)) is a clue
        what if we used binary search first on the rows then columns
        like for example for the rows we want the first value of the rows to be less than or equal to our target right
        in the first example, target 10, we know for a fact that it will not be in the 3rd row

        then from there we can also binary search within a row

        l, r = 0, len(matrix) - 1
        target_row = -1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[0][0]:
                r -= 1
            elif target > matrix[0][-1]:
                l += 1
            else:
                target_row = mid
                break

        if target_row == -1:
            return false
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[target_row][mid]:
                r -= 1
            elif target > matrix[target_row][mid]:
                l += 1
            else:
                return true
        return false
        
        """
        l, r = 0, len(matrix) - 1
        target_row = -1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r -= 1
            elif target > matrix[mid][-1]:
                l += 1
            else:
                target_row = mid
                break

        if target_row == -1:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[target_row][mid]:
                r -= 1
            elif target > matrix[target_row][mid]:
                l += 1
            else:
                return True
        return False
        