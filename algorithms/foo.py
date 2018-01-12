class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
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
                
        
assert Solution().lengthOfLongestSubstringKDistinct("eceba",2) == 3
assert Solution().lengthOfLongestSubstringKDistinct("aa",1) == 2