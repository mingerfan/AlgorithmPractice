from typing import List
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:

    @staticmethod
    def two_sum(nums: List[int], left: int, right: int, target: int) -> List[int]:
        res = []
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                res.append([left, right])
                left += 1
                right -= 1
        return res
        

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b =  self.two_sum(numbers, 0, len(numbers) - 1, target)[0]
        return [a+1, b+1]
# @lc code=end

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))