class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        palindrome:
        - remove all alphanumeric characters, case insensitive
        -> confirm aba? is a palindrome because we only care about aba

        so after ignoring the non-alphanumerics what to do
        brute force is to get a reversed version and actually remove the bad characters
        then do equality but that is like O(n) space and time 

        however we can optimize on space with the original string

        such as tracking equality from both ends using pointers
        Was it a car or a cat I saw?
        ^                          ^
        then to make it even more efficient we ignore the non an characters by just moving the pointer inward
        rather than doing some removal operation

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and  not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True
        
        """
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        