from typing import List

#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        prefix = 1
        for i in range(len(nums) - 2, -1, -1):
            result[i] = result[i + 1] * nums[i + 1]
        for i in range(0, len(nums)):
            result[i] = result[i] * prefix
            prefix *= nums[i]
        return result

# @lc code=end

a = Solution()
print(a.productExceptSelf([1, 1, 2, 1, 1]))