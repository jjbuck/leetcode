class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Use a binary search to pick the middle element from nums1. For
        this guess to be the overall median of the combined array sorted(nums1,nums2)
        an equal number of elements must be less than and greater than the guess.
        Count the number of elements in nums1 to the left of the guess, and subtract
        this number from the overall length of the combined array. This provides the
        number of elements in nums2 that the guess must be greater than. The guess
        must also be less than the next element in nums2. If this fails, repeat the
        algorithm starting in nums2.
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = self.findMedian(nums1, nums2)
        if median == None:
            median = self.findMedian(nums2,nums1)
        return median
        
    def findMedian(self, A, B):
        m = len(A)
        n = len(B)
        L = len(A) + len(B) # length of combined array
        median_idx = L // 2 # index of median in hypothetical sorted combined array
        lo = 0
        hi = m
        while lo < hi:
            guess_idx = (m-1)//2
            guess_idx = (lo + hi)//2
            guess = A[guess_idx]
            size_left = guess_idx # number of values to left of guess in first list
            size_right = m - guess_idx - 1 # number of values to right of guess in first list
            nums2_idx = n - size_left - 1
            nums2_idx = median_idx - size_left - 1
            if 0 < nums2_idx and :
                if B[nums2_idx] < guess and guess < B[nums2_idx + 1]:
                    return guess
                else:
                    if guess < B[nums2_idx]:
                        lo = lo + 1
                    else:
                        hi = guess_idx
            else:
                if B[nums2_idx] < guess and guess < A[guess_idx + 1]:
                    return None
        
        
sol = Solution()
assert sol.findMedianSortedArrays([1,2,3,4,7], [0,5,6,9])  == 4     
assert sol.findMedianSortedArrays([0,5,6,9], [1,2,3,4,7]) == 4
assert sol.findMedianSortedArrays([1, 3], [2]) == 2