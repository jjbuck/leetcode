class Solution:
    def repeatedStringMatch(self, A, B):
        """
        Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
        For example, with A = "abcd" and B = "cdabcdab".
        Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
        :type A: str
        :type B: str
        :rtype: int
        """
        A_rep = A
        count= 1
        for i in range(len(B)//len(A) + 2):
            if B in A_rep:
                return count
            else:
                A_rep += A
                count += 1
        return -1
    
assert Solution().repeatedStringMatch("abcd","cdabcdab") == 3
assert Solution().repeatedStringMatch("abababaaba","aabaaba") == 3
