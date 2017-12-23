class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        Given a string, find the length of the longest substring without repeating characters.

        Examples:
    
        Given "abcabcbb", the answer is "abc", which the length is 3.
        Given "bbbbb", the answer is "b", with the length of 1.
        Given "pwwkew", the answer is "wke", with the length of 3.
        Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

        :type s: str
        :rtype: int
        """
        my_string = s
        longest_substring_length = 0
        longest_substring = ''
        while len(my_string) > 0:
            substring = '' 
            for letter in my_string:
                if letter in substring: # this letter is already used
                    break
                else: # first time encountering letter
                    substring += letter # append letter to substring
            if len(substring) > longest_substring_length: # record new record
                longest_substring = substring
                longest_substring_length = len(substring)
            my_string = my_string[1:] # throw away first letter
        return longest_substring_length
            
        
        
sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("bbbbb") == 1
assert sol.lengthOfLongestSubstring("pwwkew") == 3
        