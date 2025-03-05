from typing import List

# 写的是对的，但是会超时...


#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#


# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        words_list_len = len(words)
        s_len = len(s)
        words_set = {x: words.count(x) for x in words}
        start = 0
        end = 0
        cnt = 0
        res = []
        if s_len < word_len * words_list_len:
            return []
        exist_set = {}
        while end < s_len:
            temp = end
            end += word_len
            cur_str = s[temp:end]
            # print(f"cur_str: {cur_str}")
            # print(f"exist_set: {exist_set}, start: {start}")
            if cur_str not in words_set or (
                cur_str in exist_set and exist_set[cur_str] >= words_set[cur_str]
            ):
                start += 1
                end = start
                cnt = 0
                exist_set.clear()
            else:
                cnt += 1
                if cur_str in exist_set:
                    exist_set[cur_str] += 1
                else:
                    exist_set[cur_str] = 1
                if cnt >= words_list_len:
                    res.append(start)
                    start += 1
                    end = start
                    cnt = 0
                    exist_set.clear()
        return res

# @lc code=end

s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
