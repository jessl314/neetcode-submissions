class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        longest substring, no duplicates 

        zxyzxyz

        length: i - j + 1

        zxyzxyz
        ^  ^
        set to keep track of potential duplicates 

        if the character is not in the set then we can continue tracking length
         until duplicate where we reset our set and move the left pointer to the right one

        l = 0
        max_len = 0
        unique = set()

        while r < len(s):
            # we want to keep moving forward and continue until our start is right after a duplicate character
            # duplicate detected take out any character from duplicate and before
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            # potential duplicates
            unique.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
        
        """
        l = 0
        max_len = 0
        unique = set()

        for r in range(len(s)):
            # we want to keep moving forward and continue until our start is right after a duplicate character
            # duplicate detected take out any character from duplicate and before
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            # potential duplicates
            unique.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len