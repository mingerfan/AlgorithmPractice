#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        cnt = 0
        op_map = [
            {1: "I", 5: "V", 4: "IV", 9: "IX"},
            {1: "X", 5: "L", 4: "XL", 9: "XC"},
            {1: "C", 5: "D", 4: "CD", 9: "CM"},
            {1: "M"},
        ]
        while num > 0:
            cur_digit = num % 10
            num //= 10
            if cur_digit == 0:
                cnt += 1
                continue
            if cur_digit == 9 or cur_digit == 4 or cur_digit == 5 or cur_digit == 1:
                temp = op_map[cnt][cur_digit]
            elif cur_digit < 4:
                temp = op_map[cnt][1] * cur_digit
            else:
                temp = op_map[cnt][5] + op_map[cnt][1] * (cur_digit - 5)
            res = temp + res
            cnt += 1
        return res


# @lc code=end

a = Solution()
print(a.intToRoman(3749))
print(a.intToRoman(3))
print(a.intToRoman(58))
print(a.intToRoman(1994))
print(a.intToRoman(9))
