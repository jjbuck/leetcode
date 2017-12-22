# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        addTwoNumbers([2,4,3],[5,6,4])
        >>> [7,0,8]
        

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        init = ListNode(0) # initialize a list node
        current = init
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry = carry + l1.val # add current value of list node to carried column
                l1 = l1.next
            if l2:
                carry = carry + l2.val # add current value of list node to carried column
                l2 = l2.next
            current.next = ListNode(carry%10) # compute carry modulo 10 and append to List Node
            current = current.next
            carry //=10 # get 10's place of current carry value

        return init.next