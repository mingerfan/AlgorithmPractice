#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        has_letter = False
        end_space_len = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                has_letter = True
                continue
            if s[i] == ' ' and not has_letter:
                end_space_len += 1
            elif s[i] == ' ' and has_letter:
                return len(s) - i - 1 - end_space_len
            
        return len(s) - end_space_len
# @lc code=end

