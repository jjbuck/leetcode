class Solution:
    def reverseString(self, s):
        """
        Write a function that takes a string as input and returns the string reversed.

        Example:
        Given s = "hello", return "olleh".
        :type s: str
        :rtype: str
        """
        reverse = s[::-1]
        return reverse