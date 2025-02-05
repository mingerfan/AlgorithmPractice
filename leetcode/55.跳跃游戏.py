from typing import List

#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(0, len(nums) - 1):
            if farthest < i:
                break
            farthest = farthest if farthest > i + nums[i] else i + nums[i]
        return farthest >= (len(nums) - 1)


# @lc code=end
