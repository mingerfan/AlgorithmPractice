from typing import List
#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        rl_sum = 0
        start = 0
        end = 0
        nums_len = len(nums)
        min_len = nums_len + 1
        while end < nums_len:
            rl_sum += nums[end]
            while rl_sum >= target:
                start_num = nums[start]
                if rl_sum - start_num >= target:
                    rl_sum -= start_num
                    start += 1
                else:
                    min_len = min(min_len, end - start + 1)
                    break
            end += 1
                

        return min_len if min_len != nums_len + 1 else 0


# @lc code=end

s = Solution()
print(s.minSubArrayLen(7, [2, 4, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
