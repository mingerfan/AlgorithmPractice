from typing import List
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start

# 这个解法应该是对的，但是会超时
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0 for _ in range(0, len(prices) + 1)]
        for i in range(2, len(prices) + 1):
            prof_max = -100000000
            for j in range(1, i):
                max_one_sell_profit = prices[i - 1] - min(prices[j - 1 : i])
                profit = dp[j] + max_one_sell_profit
                prof_max = prof_max if prof_max > profit else profit
            dp[i] = prof_max
        return max(dp)


# @lc code=end
