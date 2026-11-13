class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        questions I could ask: will I get a non int value? what should I return if list is empty?
        space? time?

        plan: frequency map (dictionary) where key is element of nums and value is amount of time it appears
        if the item not in the dictionary, continue, if it is return true. at the end return false
        because no duplicates were found
        """
        # base case: empty list
        if not nums:
            return False
        freq = {}
        for num in nums:
            if num in freq:
                return True
            freq[num] = 0
        return False
         