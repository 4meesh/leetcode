class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        rev = filtered[::-1]
        return rev == filtered