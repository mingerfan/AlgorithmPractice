from typing import List
#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            arr = [0] * 10
            for j in i:
                if j == ".":
                    continue
                j_ = int(j)
                if arr[j_] >= 1:
                    # print(f'return False, in {i}, {j}')
                    return False
                arr[j_] += 1
        for i in range(0, 9):
            arr = [0] * 10
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                j_ = int(board[j][i])
                if arr[j_] >= 1:
                    # print(f'return False, in {board[j]}, {board[j][i]}')
                    return False
                arr[j_] += 1

        for i in range(0, 3):
            for j in range(0, 3):
                row = 0
                arr = [0] * 10
                col = 0
                while row < 3:
                    cur_row = i * 3 + row
                    col = 0
                    while col < 3:
                        cur_col = j * 3 + col
                        # print(f"cur_col: {cur_col}, cur_row: {cur_row}")
                        col += 1
                        if board[cur_row][cur_col] == ".":
                            continue
                        j_ = int(board[cur_row][cur_col])
                        if arr[j_] >= 1:
                            return False
                        arr[j_] += 1
                    row += 1
        return True


# @lc code=end

s = Solution()
print(
    s.isValidSudoku(
        [
            [".", ".", ".", ".", "5", ".", ".", "1", "."],
            [".", "4", ".", "3", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "1"],
            ["8", ".", ".", ".", ".", ".", ".", "2", "."],
            [".", ".", "2", ".", "7", ".", ".", ".", "."],
            [".", "1", "5", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "2", ".", "9", ".", ".", ".", ".", "."],
            [".", ".", "4", ".", ".", ".", ".", ".", "."],
        ]
    )
)
