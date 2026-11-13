class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        input: array of integers
        return boolean
        true: if any value appears more than once in the array otherwise return false
        the first one is true because 2 3s and the second is false because all unique

        first what to return for []? -> false
        no invalid input?

        ok first thing is that we want to discern duplicates this could be done
        two ways: dictionary frequency map, where we stop and return true if a value is already
        in it or a set, where same, if the val is in it we have found a duplicate
        I think because dictionary has to store key, val and we only need to keep track of if there is 
        one val (aka if the val has already been seen, we have our element key and then 1 as the paired value)
        we should do set since set consists of all the necessary information

        the idea then for the algorithm
        is to initialize an empty "seen" set. then loop through the elements, adding
        the element if not seen, if seen (aka element in set) we can return true
        if we make it through the entire set return false 

        this is at most O(n) memory and time since for the worst case aka unique case
        we have searched all elements and stored all elements in the set
        
        
        """

        seen = set()
        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False