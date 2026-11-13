class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """

        input: two strings
        return: boolean -> true if the strings are anagrams

        anagram: string that contains the exact same characters as another string but the
        order can be different

        empty strings (both)? true

        base: check if the lengths of the strings are different, if yes we can immediately
        return false

        my immediate thought is to sort each string and then compare
        but this is O(nlogn + mlogm) at best and if using sorted could end up being O(n + m)

        then the next thought was to make a hashmap: since if they are anagrams, same letters
        and same frequencies of said letters. then we compare the count for each element
        this reduces the memory to O(1) since there are at most 26 letters and we are only keeping
        track of count

        to make this easier, instead of two for loops we can use .get() which allows us to increment a count of each
        letter or else initializes to 0 if there is no such letter. if the two maps match at the end then we return true else return false


        
        """
        # base case: lengths match?
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        # making frequency map for both strings
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        