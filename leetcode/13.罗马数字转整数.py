#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start

from typing import Tuple


def mapFunc(c: str) -> Tuple[int, str]:
    if c.startswith("IV"):
        return 4, c[2:]
    elif c.startswith("IX"):
        return 9, c[2:]
    elif c.startswith("XL"):
        return 40, c[2:]
    elif c.startswith("XC"):
        return 90, c[2:]
    elif c.startswith("CD"):
        return 400, c[2:]
    elif c.startswith("CM"):
        return 900, c[2:]

    match c[0]:
        case "I":
            return 1, c[1:]
        case "V":
            return 5, c[1:]
        case "X":
            return 10, c[1:]
        case "L":
            return 50, c[1:]
        case "C":
            return 100, c[1:]
        case "D":
            return 500, c[1:]
        case "M":
            return 1000, c[1:]


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        while s:
            res, s = mapFunc(s)
            total += res
        return total

# @lc code=end

a = Solution()
print(a.romanToInt("III"))
print(a.romanToInt("IV"))
print(a.romanToInt("IX"))
print(a.romanToInt("LVIII"))
print(a.romanToInt("MCMXCIV"))