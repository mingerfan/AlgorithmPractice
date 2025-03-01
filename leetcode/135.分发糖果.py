from typing import List
#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_rule = [1] * n
        right_rule = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_rule[i] = left_rule[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_rule[i] = right_rule[i + 1] + 1
        ret = 0

        for i in range(n):
            ret += max(left_rule[i], right_rule[i])
        
        return ret



# @lc code=end

a = Solution()
print(a.candy([1,6,10,8,7,3,2]))