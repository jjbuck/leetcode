class Solution:
    def kEmptySlots(self, flowers, k):
        #TODO: Not solved yet.
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(flowers)-k-1):
            between = flowers[i+1:i+k+1]
            flower = flowers[i]
            next_flower = flowers[i+k+1]
            if all([check > flower for check in between]) and all([check > next_flower for check in between]):
                return i+k+1
        return -1
            
        
assert Solution().kEmptySlots([1,3,2],1) == 2
assert Solution().kEmptySlots([1,2,3],1) == -1
assert Solution().kEmptySlots([6,5,8,9,7,1,10,2,3,4],2) == 8