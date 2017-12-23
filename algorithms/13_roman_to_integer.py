class Solution:
    def romanToInt(self, s):
        """
        Given a roman numeral, convert it to an integer.
        Input is guaranteed to be within the range from 1 to 3999.
        :type s: str
        :rtype: int
        """
        s = s.lower() # convert to lowercase
        roman_dict = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}
        eq_int = 0 # store equivalent integer
        roman = s
        beg = '' # initialize first character in the roman numeral
        while len(roman) > 0:
            this_int = roman_dict[roman[0]] # look this character up in the dict
            if len(roman) > 1:
                next_int = roman_dict[roman[1]] # 'look ahead' to next integer
                if next_int <= this_int: # add this int as-is
                    eq_int += this_int
                    roman = roman[1:]
                else: # next_int > this_int
                    eq_int += (next_int - this_int) # then the numeric representation is the next int minus the current int
                    roman = roman[2:]
            else:
                eq_int += this_int
                roman = roman[1:]
        return eq_int
            
        
sol = Solution()
assert sol.romanToInt('i') == 1
assert sol.romanToInt('ii') == 2
assert sol.romanToInt('iii') == 3
assert sol.romanToInt('v') == 5
assert sol.romanToInt('vi') == 6
assert sol.romanToInt('x') == 10
assert sol.romanToInt('ix') == 9
assert sol.romanToInt('MCMXCV') == 1995