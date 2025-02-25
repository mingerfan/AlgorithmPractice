from typing import List
#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#


# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rela_cost = list(map(lambda p: p[0] - p[1], zip(gas, cost)))
        cnt = 0
        target = -1
        start = 0
        while cnt < len(rela_cost):
            cnt1 = 0
            tank = 0
            while cnt1 < len(rela_cost):
                cur_idx = start + cnt1 if start + cnt1 < len(rela_cost) else start + cnt1 - len(rela_cost)
                gas_added = rela_cost[cur_idx]
                tank += gas_added
                cnt1 += 1
                if tank < 0:
                    if start + cnt1 < len(rela_cost):
                        start = cur_idx + 1
                    break
            if cnt1 == len(rela_cost) and tank >= 0:
                target = start
            cnt += 1
        return target


# @lc code=end

a = Solution()
print(a.canCompleteCircuit([4,3,8,6,5], [5,8,4,7,7]))
