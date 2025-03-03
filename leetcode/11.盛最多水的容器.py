from typing import List
#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] > height[right]:
                cur_water = height[right] * (right - left)
                right -= 1
            else:
                cur_water = height[left] * (right - left)
                left += 1

            if cur_water > max_water:
                max_water = cur_water
        return max_water

# @lc code=end

