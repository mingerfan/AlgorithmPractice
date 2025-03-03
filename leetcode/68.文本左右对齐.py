from typing import List

#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#


# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res_list = []
        words_index = 0
        while words_index < len(words):
            res_str = ""
            len_cnt = 0
            words_len = 0
            line_max_words = 0
            last_line = False
            while len_cnt <= maxWidth:
                word_len = len(words[words_index + line_max_words])
                if len_cnt + word_len <= maxWidth:
                    words_len += word_len
                    len_cnt += word_len + 1
                    line_max_words += 1
                    if len_cnt == maxWidth + 1 or words_index + line_max_words == len(words):
                        len_cnt -= 1
                        last_line = True
                        break
                else:
                    len_cnt -= 1
                    break
            total_gap = maxWidth - words_len
            over_cnt = 0
            if last_line:
                ave_gap = 1
                over_cnt = 0
            else:
                if line_max_words > 1:
                    ave_gap = total_gap // (line_max_words - 1)
                    over_cnt = total_gap - ave_gap * (line_max_words - 1)
                else:
                    ave_gap = 0
                    over_cnt = 0
            temp = 0
            gap_cnt = 0
            while temp < line_max_words:
                res_str += words[words_index + temp]
                if temp == line_max_words - 1:
                    res_str += " " * (total_gap - gap_cnt)
                else:
                    if over_cnt != 0:
                        res_str += " " * (ave_gap + 1)
                        gap_cnt += ave_gap + 1
                        over_cnt -= 1
                    else:
                        res_str += " " * ave_gap
                        gap_cnt += ave_gap
                temp += 1
            # print(f'last_line: {last_line}, {res_str}')
            res_list.append(res_str)
            # print(f'len_cnt: {len_cnt}, words_len: {words_len}')
            words_index += line_max_words
        return res_list


# @lc code=end

a = Solution()
print(
    a.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
)
print(a.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(
    a.fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
)
