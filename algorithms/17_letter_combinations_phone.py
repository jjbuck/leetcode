class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if digits == '':
            letters = []
        else:
            letters = ['']
        for digit in digits:
            letters = [x+y for y in digit_map[digit] for x in letters]
        return letters
    
assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]