#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char.lower() for char in s if char.isalpha() or char.isdigit()])
        s1 = s[::-1]
        # print(s1)
        return s1 == s
# @lc code=end

s = Solution()
print(s.isPalindrome("0P"))