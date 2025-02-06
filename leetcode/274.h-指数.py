from typing import List
#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_c = sorted(citations, reverse=True)
        sorted_c.append(0)
        h_index = 0
        for idx, cnt in enumerate(sorted_c):
            if cnt == idx + 1:
                h_index = cnt
                break
            elif cnt < idx + 1:
                h_index = idx
                break
        return h_index


# @lc code=end

a = Solution()
print(a.hIndex([100]))
