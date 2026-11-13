class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """

        input an array of strings and we want to group all anagrams together into respective sublists
        then just return the nested list

        anagram: same characters and I assume length as another string
        so like "act" and "cat" would count

        then if there is only one string we just make a sublist for that string and return it like that?

        my first thought is that we would make a map and sort each string. the key is the sorted version and the values
        are a list of the original strings

        this ends up being O(m * nlogn) time for iterating through m items and sorting each item and O(m) because we end up
        storing each item in dictionary
        
        """
        gram_map = {}

        for s in strs:
            sorte = ''.join(sorted(s))
            if sorte not in gram_map:
                gram_map[sorte] = [s]
            else:
                gram_map[sorte].append(s)
        return list(gram_map.values())

