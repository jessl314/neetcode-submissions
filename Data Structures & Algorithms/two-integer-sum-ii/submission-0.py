class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        integer array, sorted in non-decreasing order -> hint!
        can it start negative??? 

        return 1-index array of two numbers tht add to a given target number. annot use same element twice
        (the values could be duplicates??) -> one valid solution
        O(1)

        O(1) no creating some additional results array 
        [1,2,3,4]
        1+2 = 3 and the indices in one index are 1,2
        brute force: for loop and check every combo where index 1 != index2 so that would be like O(n^2)

        [1,2,3,4] target = 6

        so we want to keep track of two numbers at a time and go through all elements

        so what if we had a pointer at either end:

        1 2 3 4
        ^     ^
        then check the sum. if it is too small then we move our left pointer (the smaller value)
        inwards and the opposite if the sum is too much. if it is equal than our array is [i + 1, j + 1] so do
        keep track of indices and there is no non-solution but return [] as a safety net

        result = []
        l, r = 0 , len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        """
        l, r = 0 , len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []

        