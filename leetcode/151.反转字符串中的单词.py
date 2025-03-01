#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        res = s.split()
        res.reverse()
        return ' '.join(res)
# @lc code=end

a = Solution()
print(a.reverseWords("the sky is blue"))
print(a.reverseWords(" hello world "))
print(a.reverseWords("a good   example"))
