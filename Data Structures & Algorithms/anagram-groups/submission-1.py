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

        what if we want to reduce to m time?

        well what we really want in a anagram is that they have the same frequency of each letter from alphabet
        so maybe instead of sorting we can make a frequency map for the letters?
        
        """
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return list(result.values())

