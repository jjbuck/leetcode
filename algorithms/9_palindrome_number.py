class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        ints = [int(digit) for digit in str(x)] # split integer into list of integers
        ints.reverse() # reverse the list of integers
        ints_rvrs = ''.join(str(digit) for digit in ints) # convert list to string
        ints_rvrs = int(ints_rvrs) # convert string to int
        if ints_rvrs > 2**31: # check to see if exceeds 32-bit limit
            ints_rvrs = 0
        ints_rvrs = sign * ints_rvrs # reapply sign
        if x == ints_rvrs:
            palindrome = True
        else:
            palindrome = False
        return palindrome
        
sol = Solution()
assert sol.isPalindrome(123) == False
assert sol.isPalindrome(121) == True
assert sol.isPalindrome(-121) == False
assert sol.isPalindrome(-2147447412) == False