"""
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
"""
# O(n^2)
class Solution:
    def test(s):
        n = len(s)
        flag  = True 
        for i in range(0,(n//2)):
            if s[i]!=s[n-i-1]:
                flag = False
                return flag
        return flag
    
    def longestPalindrome(self, s: str) -> str:
        lst1 = [] #store the str
        lst2 = [] #store the len
        n = len(s)
        if n<=1:
            return s
        else:
            for i in range(0,n):
                for j in range(i+1,n):
                    if s[j] == s[i]:
                        substr = s[i:j+1]
                        if Solution.test(substr):
                            lst1.append(substr)
                            lst2.append(len(substr))
            if lst2 == []: #没有回文
                return s[0]
            else:
                max_index = lst2.index(max(lst2))
                return lst1[max_index]

            
sl = Solution()
print(sl.longestPalindrome("babad"))


#
