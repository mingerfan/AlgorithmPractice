from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        mid = (right + left) // 2
        while left < right:
            if target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                left = mid + 1
            mid = (right + left) // 2
        return right

a = Solution()
print(a.search([-1,0,3,5,9,12], 9))
