class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False