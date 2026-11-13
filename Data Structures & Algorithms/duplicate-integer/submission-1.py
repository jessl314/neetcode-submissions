class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        input: array called nums which consists of integers
        return: Boolean, true if any value appears more than once in the array
        otherwise false

        questions: could array be empty? what to do? will there be any invalid input?

        first thought is to create a frequency map while iterating through entire list

        then the idea is to return true if a number is already in the map as key

        for i in range(len(nums)):
            if nums[i] is in freq:
                return true
            continue

        logistically this makes sense but intuitively less so since we unnessarily keep a pair

        so I would change to set instead of dictionary

        both would be O(n) time/memory and there isn't really a way to optimize this due to needing to
        visit every number. sorting wouldn't help because of a case like this [1,2,3,3,4,5,5]

        plan: is to create an empty set and then loop through nums. if number isnot in set
        we add it else we return true. if we never return true then we know that there is no duplicate
        
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False