#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        slen = len(s)
        if slen == 0:
            return True
        for i in t:
            if s[s_idx] == i:
                s_idx += 1
            if s_idx == slen:
                return True
        return False
# @lc code=end