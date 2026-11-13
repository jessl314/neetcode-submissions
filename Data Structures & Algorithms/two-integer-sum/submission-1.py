class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        understanding:
        empty list?
        space requirements?
        time requirements?
        brute force: O(n^2) solution: do a nested for loop and compare each digit
        with every other digit....

        planning:

        hash map:

        maybe keep a dictionary where the key is the difference of the element i from target and value is i
        if at any point element i is in this dictionary then return the value from the corresponding key-value pair
        and i in a list

        """

        diff = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in diff:
                return [diff[difference], i]
            diff[num] = i
        
                    