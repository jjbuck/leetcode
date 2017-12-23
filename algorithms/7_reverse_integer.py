class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        ints = [int(digit) for digit in str(x)] # split integer into list of integers
        ints.reverse()
        ints_rvrs = ''.join(str(digit) for digit in ints) # convert list to string
        ints_rvrs = int(ints_rvrs) # convert string to int
        if ints_rvrs > 2**31: # check to see if exceeds 32-bit limit
            ints_rvrs = 0
        ints_rvrs = sign * ints_rvrs # reapply sign
        return ints_rvrs
    
        
sol = Solution()
assert sol.reverse(123) == 321
assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21
assert sol.reverse(1534236469) == 0
assert sol.reverse(1563847412) == 0
