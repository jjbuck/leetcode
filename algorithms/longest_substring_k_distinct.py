class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Given a string, find the length of the longest substring T that contains at most k distinct characters.
        For example, Given s = “eceba” and k = 2,
        T is "ece" which its length is 3.
        :type s: str
        :type k: int
        :rtype: int
        """
        
        # Brute force approach
        '''
        if len(s) == 1 and k <= len(s):
            return k
        elif len(s) == 1 and k > len(s):
            return len(s)
        longest_substr = ''
        for i in range(len(s)):
            substr = s[i]
            j = 0
            while len(set(substr)) <= k and (i+j) < (len(s)):
                
                if len(substr) > len(longest_substr):
                    longest_substr = substr
                j += 1
                if (i+j) >= len(s):
                    break
                substr += s[i+j]
        return len(longest_substr)
        '''
    
        # Sliding window approach - time limit exceeded
        '''
        left = right = 0
        longest_substr = 0
        for _ in range(len(s) + 1):
            substr = s[left:right]
            while len(set(substr)) > k:
                left += 1
                substr = s[left:right]
            longest_substr = max(len(substr), longest_substr)
            right += 1
        return longest_substr
        '''
        # Sliding window hash table
        d = {}
        low, longest_substr = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            longest_substr = max(i - low + 1, longest_substr)
        return longest_substr
                
                
        
assert Solution().lengthOfLongestSubstringKDistinct("eceba",2) == 3
assert Solution().lengthOfLongestSubstringKDistinct("aa",1) == 2
        