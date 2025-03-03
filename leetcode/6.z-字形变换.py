#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ''
        cnt = 0
        period = numRows * 2 - 2
        while cnt < numRows:
            j = cnt
            while j < len(s):
                space = period - cnt * 2
                res += s[j]
                if space != 0 and space != period and j + space < len(s):
                    res += s[space + j]
                j += period
            cnt += 1
        return res

# @lc code=end

s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("A", 1))