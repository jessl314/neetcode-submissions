class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       """

       input: array of integers, a separate integer 

       return two indices i and j such that the sum of the elements equal target but the indices
       are also different

       so example 1: 3 + 4 = 7, so return indices 0,1

       there will always be an answer -> so list must always be >= 2 in length

       well we want the indices in order meaning we need to search in order
       for the first example say we look at 3, we then know that we need to find a 4
       since 7 - 4 = 3. this makes me think hashmap/dictionary since we want to know
       two things at once, what integer we are currently looking at and what is the remaining
       number to look for. we also want to know the index at all times so maybe this first hash map
       idea does not make sense

       what if instead we make a hash map with the num as a key and index as a value
       then loop through nums again and calculate difference between target and num
       if the difference in this dictionary (also indices of the values not in there)
       then we have found a match and can return the current index and the index of the difference
       value which will always have a greater index to satisfy the smaller index first

       O(n) time and memory since we at worst go through every element and we also store all elements


       
       
       
       """     
       differences = {}

       # most recent index map
       for i, n in enumerate(nums):
            differences[n] = i   
       for i, n in enumerate(nums):
        diff = target - n
        if diff in differences and differences[diff] != i:
            return [i, differences[diff]]
       return []

              