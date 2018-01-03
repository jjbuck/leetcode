class Solution:
    def plusOne(self, digits):
        """
        Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
        You may assume the integer do not contain any leading zero, except the number 0 itself.
        The digits are stored such that the most significant digit is at the head of the list.
        :type digits: List[int]
        :rtype: List[int]
        """
        list_of_str = [str(digit) for digit in digits]
        int_str = ''.join(list_of_str)
        int_num = int(int_str)
        plus_one = int_num + 1
        plus_one_str = str(plus_one)
        plus_one_str_list = [c for c in plus_one_str]
        plus_one_int_list = [int(s) for s in plus_one_str_list]
        return plus_one_int_list
        