class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        L = len(A) + len(B)
        if L % 2 == 1: # odd length, so median will be element at midpoint
            return self.getKth(A, B, L//2 + 1)
        else: # even length, so median will be average of two elements on either side of midpoint
            return (self.getKth(A, B, L//2) +  self.getKth(A,B, L//2 + 1)) * 0.5

    def getKth(self, A, B, k): # get element at kth value of merged array
        m, n = len(A), len(B)
        if m > n:
            return self.getKth(B, A, k)

        left, right = 0, m    
        while left < right:
            mid = left + (right - left) // 2 # new midpoint in A
            # first conditional - check that k-1-mid gives index in B
            # second conditional - check that the midpoint of A is greater than the midpoint of B
            if 0 <= k - 1 - mid < n and A[mid] >= B[k - 1 - mid]:
                right = mid # need to shift right point down to mid
            else:
                left = mid + 1 # need to shift left point up to mid

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)
        
assert Solution().findMedianSortedArrays([1,2,3,4,7], [0,5,6,9])  == 4     
assert Solution().findMedianSortedArrays([0,5,6,9], [1,2,3,4,7]) == 4
assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5