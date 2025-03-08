from typing import List
#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 1
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        row = 0
        col = 0
        res = []
        dirction = 0 # 0 for l -> r, 1 for t -> d, 2 for r -> left, 3 for d -> t
        total = (down + 1) * (right + 1)
        while total > 0:
            res.append(matrix[row][col])
            total -= 1
            # print(f"direction: {dirction}, left: {left}, right: {right}, top: {top}, down: {down}")
            match dirction:
                case 0:
                    col += 1
                    if col > right:
                        col = right
                        row += 1
                        right -= 1
                        dirction = 1
                case 1:
                    row += 1
                    if row > down:
                        row = down
                        col -= 1
                        down -= 1
                        dirction = 2
                case 2:
                    col -= 1
                    if col < left:
                        col = left
                        row -= 1
                        left += 1
                        dirction = 3
                case 3:
                    row -= 1
                    if row < top:
                        row = top
                        col += 1
                        top += 1
                        dirction = 0
        return res
 
# @lc code=end

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))