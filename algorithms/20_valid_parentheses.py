class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_pair = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in char_pair.values():
                stack.append(char)
            if char in char_pair.keys():
                if stack == [] or char_pair[char] != stack.pop(): # if stack is empty or if pair for current char is not in stack
                    return False
        return stack == [] # only true if stack has been emptied, i.e., all parentheses paired


assert Solution().isValid("()") == True
assert Solution().isValid("()[]{}") == True
assert Solution().isValid("(]") == False
assert Solution().isValid("[") == False