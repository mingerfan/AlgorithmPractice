from typing import List
#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#


# @lc code=start
class Solution:
    @staticmethod
    def two_sum(nums: List[int], left: int, right: int, target: int) -> List[List[int]]:
        res = []
        hashset = set()
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                if nums[left] not in hashset:
                    res.append([nums[left], nums[right], -target])
                    hashset.add(nums[left])
                    hashset.add(nums[right])
                left += 1
                right -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        nums_len = len(nums)
        left_neg = 0
        right_pos = nums_len - 1
        last_num = -1
        last_idx = -1
        for idx, i in enumerate(nums):
            if last_num < 0 and i >= 0:
                left_neg = idx
            if last_num <= 0 and i > 0:
                right_pos = last_idx
            last_idx = idx
            last_num = i

        if nums[0] > 0 or nums[-1] < 0:
            return res
        
        if right_pos - left_neg + 1 >= 3:
            res.append([0, 0, 0])
        # print(f'{nums}, left_neg: {left_neg}, right_pos: {right_pos}')
        hashset = set()
        for i in range(right_pos + 1, nums_len):
            if nums[i] in hashset:
                continue
            if nums[right_pos] != 0:
                temp = self.two_sum(nums, 0, left_neg - 1, -nums[i])
            else:
                temp = self.two_sum(nums, 0, left_neg, -nums[i])
            hashset.add(nums[i])
            res.extend(temp)
        hashset = set()
        for i in range(0, left_neg):
            if nums[i] in hashset:
                continue
            temp = self.two_sum(nums, right_pos + 1, nums_len - 1, -nums[i])
            hashset.add(nums[i])
            res.extend(temp)
        return res


# @lc code=end

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([0, 1, 1]))
print(s.threeSum([0, 0, 0]))
print(s.threeSum([1, 1, -2]))
print(s.threeSum([-2,0,0,2,2]))
