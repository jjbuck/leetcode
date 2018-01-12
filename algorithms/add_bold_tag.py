class Solution:
    def addBoldTag(self, s, dict):
        """
        Strategy: Build boolean array by traversing array to indicate whether a letter should be bold.
        Then traverse array again and add bold tags based on boolean
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bold = [False] * len(s)
        for d in dict:
            pos = 0
            while s.find(d) != -1:
                ind = s.find(d, pos)
                if ind == -1:
                    break
                bold[ind:(ind+len(d))] = [True for item in bold[ind:(ind+len(d))]]
                pos += 1
        # Now traverse array again to add bold tags based on boolean
        new_str = ''
        flag = False # used to indicate start or end of bold tag
        for i in range(len(s)):
            if bold[i] == True and flag == False: # add new bold tag
                new_str += '<b>'
                flag = True
            if bold[i] == False and flag == True:  # need to close bold tag
                new_str += '</b>'
                flag = False
            new_str += s[i]
        if flag == True:
            new_str += '</b>'
        return new_str
                
    
assert Solution().addBoldTag("abcxyz123",["abc","123"]) == "<b>abc</b>xyz<b>123</b>"
assert Solution().addBoldTag("aaabbcc",["aaa","aab","bc"]) == "<b>aaabbc</b>c"
assert Solution().addBoldTag("aaabbcc",["a","b","c"]) == "<b>aaabbcc</b>"
                
                