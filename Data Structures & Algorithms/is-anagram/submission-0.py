class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        questions:
        what to do with empty string?
        
        
        making a frequency map for each and then checking
        to see if the maps are the same

        """

        s_freq = {}
        t_freq = {}

        for i in s:
            if i not in s_freq:
                s_freq[i] = 1
            s_freq[i] += 1
        
        for j in t:
            if j not in t_freq:
                t_freq[j] = 1
            t_freq[j] += 1
        
        for k in t_freq:
            # 1st case a letter that appears in t_freq does not in s_freq
            if k not in s_freq:
                return False
            # 2nd case: a letter appears in both but is not same freq
            elif t_freq[k] != s_freq[k]:
                return False
        return True
        