from typing import List

#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_len = 0
        for i in range(len(strs[0])):
            target = strs[0][i]
            is_match = True
            for j in range(1, len(strs)):
                is_match &= i < len(strs[j]) and strs[j][i] == target
                if not is_match:
                    break
            if is_match:
                longest_len += 1
            else:
                break
        return strs[0][:longest_len]
        
# @lc code=end

a = Solution()
print(a.longestCommonPrefix(["flower","flow","flight"]))
print(a.longestCommonPrefix(["dog","racecar","car"]))