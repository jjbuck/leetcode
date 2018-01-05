class Solution:
    def singleNumber(self, nums):
        """
        Given an array of integers, every element appears twice except for one. Find that single one.
        Note:
        Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
        :type nums: List[int]
        :rtype: int
        """
        check = 0
        for num in nums:
            check ^= num
        return check
    
assert Solution().singleNumber([1,1,3]) == 3
assert Solution().singleNumber([1,3,1]) == 3