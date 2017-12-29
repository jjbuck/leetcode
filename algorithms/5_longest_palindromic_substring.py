class Solution:
    def longestPalindrome(self, s):
        """
        Given a string s, find the longest palindromic substring in s. 
        You may assume that the maximum length of s is 1000.
        :type s: str
        :rtype: str
        """
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and self.isPalindrome(s[i-maxLen-1:i+1]):
            		start=i-maxLen-1
            		maxLen+=2
            if i-maxLen >=0 and self.isPalindrome(s[i-maxLen:i+1]):
            		start=i-maxLen
            		maxLen+=1
        return s[start:start+maxLen]
    
    def isPalindrome(self,s):
        if s == s[::-1]:
            return True
        else:
            return False



    
assert Solution().longestPalindrome('babad') == 'bab' or Solution().longestPalindrome('babad') == 'aba'
assert Solution().longestPalindrome('a') == 'a'
assert Solution().longestPalindrome('bb') == 'bb'
                
                
                
            
        