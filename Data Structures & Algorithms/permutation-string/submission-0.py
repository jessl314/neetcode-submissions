class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        
        brute force: check every substring len(s) then sort and compare to sorted s1
        nlogn * n^2 for checking every substring

        keep track of the letters (only need frequency) via a freq map 
        this is O(1) since only 26 letters 
        naive since we need to constantly keep track of number of letters needed
        freqmap for s1
        # need x amount of letters
        need_count = len(s1)
        for r in range(len(s2)):
            freqmap2, cur = 0
            freqmap2[s2[r]] = freqmap2.get(s2[r], 0) +  1

            if s1[r] < s2[r]:
                keep going and adding more to freqmap2
            if s1[r] == s2[r]:
                cur += 1
            if cur = need:
                we have found all letters -> True
        return False 

        but the size is fixed so what if we do somehting like
        overall the idea is to have the substring match like boolean all the letters right
        so in the first ex: a,b,c are 1 and all else are zeroes
        to keep track of boolean 
        make two 26 element arrays [0]*26 then for each letter considering s1 characters only
         we add a 1 if present as a start line
         [1,1,1,0,0,0...]
         [0,0,1,0000]

        then matches we add one for each s1[i] = s2[i] 
        23 matches

        l = 0 then increment in loop 
        and do for r in range(len(s1), len(s2))
        if we already have 26 matches return true
        check the current index character
        increment the count if this count is same as the count from 
        
        """
        a1, a2 = [0] * 26, [0] * 26
        # checking if s1 == s2
        for c in range(len(s1)):
            a1[ord(s1[c]) - ord('a')] += 1
            a2[ord(s2[c]) - ord('a')] += 1
        if a1 == a2:
            return True
        # we are checking the rest of possibilities
        for r in range(len(s1), len(s2)):
            a2[ord(s2[r]) - ord('a')] += 1
            a2[ord(s2[r - len(s1)]) - ord('a')] -= 1
            if a1 == a2:
                return True
        return False
        