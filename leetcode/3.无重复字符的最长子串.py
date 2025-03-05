#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_dict = {}
        start = 0
        end = 0
        max_len = 0
        s_len = len(s)
        while end < s_len:
            c_end = s[end]
            if c_end not in c_dict or c_dict[c_end] < start:
                max_len = max(max_len, end - start + 1)
                c_dict[c_end] = end
                end += 1
            elif c_end in c_dict and c_dict[c_end] >= start:
                start = c_dict[c_end] + 1
            else:
                print("Should not reach here")
                assert(False)
        return max_len

                
# @lc code=end

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))