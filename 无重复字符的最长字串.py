"""
无重复字符的最长子串
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0            #最长不重复子串的长度
        res=""           #用来存储不重复子串的临时变量
        for i in s:      #遍历
            if i not in res:       #如果不在临时变量中，加上
                res+=i
            else:
                res=res[res.index(i)+1:]    #遇到重复的，通过切片更新和添加更新临时变量
                res+=i
            ans=max(ans,len(res))    #每次遍历结束，更新最长不重复子串的长度
        return ans



sl = Solution()
print(sl.lengthOfLongestSubstring("aab"))