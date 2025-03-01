from typing import List
#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        decreasing_blocks = []
        for i in range(len(height)):
            # print(decreasing_blocks)
            last_pop_height, last_pop_idx = decreasing_blocks.pop() if len(decreasing_blocks) > 0 else (-1, -1)
            if last_pop_height > height[i]:
                decreasing_blocks.append((last_pop_height, last_pop_idx))
                decreasing_blocks.append((height[i], i))
                continue
            while True:
                cur_pop_height, cur_pop_idx = decreasing_blocks.pop() if len(decreasing_blocks) > 0 else (-1, -1)
                if cur_pop_height == -1:
                    break
                calc_height = min(cur_pop_height, height[i]) - last_pop_height
                # print(f'calc_height: {calc_height}')
                res += (i - cur_pop_idx - 1) * calc_height
                if height[i] < cur_pop_height:
                    decreasing_blocks.append((cur_pop_height, cur_pop_idx))
                    break
                last_pop_height, last_pop_idx = cur_pop_height, cur_pop_idx

            decreasing_blocks.append((height[i], i))

        return res


# @lc code=end

a = Solution()
print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(a.trap([4, 2, 0, 3, 2, 5]))
