class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        input: strings s and t. 
        return: true if the two strings are anagrams, otherwise return false

        anagram: a string that contains the exact same characters as another string
        but the order is different

        what type of characters are in this string?

        base case across the board: if the length of the strings are different then
        we can immediately return false

        my first thought is to sort strings and compare if they are the same after
        this should work as we are basically sorting by ascii

        the problem here is that this approach is at best nlogn time because of sorting

        not only that but it is O(n) memory if want to do booleaan we should be using sorted()

        so what I can think is of is that O(n) memory will be the same because we
        do need to visit every character in both strings

        but we can optimize the time complexity. 
        the first thing that I would do for this is to make frequency maps for both s and t

        jar: j: 1, a:1, r:1
        jam: j:1, a:1, m:1

        now since dictionaries are not ordered
        we do have to do another loop

        for i in jar:
            check if i is in jam
        
        and if not then we return false

        otherwise after loop return true
        
        """
        # base case: length of strings does not match
        if len(s) != len(t):
            return False
        
        # making frequency maps
        s_freq = {}
        
        for i in s:
            if i in s_freq:
                s_freq[i] += 1
            else:
                s_freq[i] = 1
        
        t_freq = {}
        
        for j in t:
            if j in t_freq:
                t_freq[j] += 1
            else:
                t_freq[j] = 1
        
        # we are comparing frequency maps

        for k in s_freq:
            # character is not matching
            if k not in t_freq:
                return False
            elif s_freq[k] != t_freq[k]:
                return False
        # bbcc ccbc     b: 2, c: 2  vs. c: 3, c: 1
        return True
        


