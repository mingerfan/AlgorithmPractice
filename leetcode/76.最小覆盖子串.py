#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed_letter = [0] * 52
        cnt_map = [0] * 52

        def li(letter):
            if "a" <= letter <= "z":  # 小写字母
                return ord(letter) - ord("a")  # 映射到 0-25
            elif "A" <= letter <= "Z":  # 大写字母
                return ord(letter) - ord("A") + 26  # 映射到 26-51
            else:
                raise ValueError("输入必须是字母")

        target_cnt = 0
        for i in t:
            needed_letter[li(i)] += 1
            target_cnt += 1

        cnt = 0
        min_start = 0
        min_end = 0
        s_len = len(s)
        min_len = s_len + 1
        start = 0
        end = 0
        while end < s_len:
            # print(f"start: {start}, end: {end}, cnt: {cnt}, target: {target_cnt}")
            cur_end_idx = li(s[end])
            if needed_letter[cur_end_idx] > 0:
                if needed_letter[cur_end_idx] > cnt_map[cur_end_idx]:
                    cnt += 1
                cnt_map[cur_end_idx] += 1
            if cnt == target_cnt:
                # print("enter")
                # 开始枚举start
                cur_start_idx = li(s[start])
                while needed_letter[cur_start_idx] <= 0 or (
                    needed_letter[cur_start_idx] > 0
                    and needed_letter[cur_start_idx] < cnt_map[cur_start_idx]
                ):
                    if needed_letter[cur_start_idx] > 0:
                        cnt_map[cur_start_idx] -= 1
                    start += 1
                    cur_start_idx = li(s[start])
                # print(f'--- start: {start}, end: {end}, cnt: {cnt}, target: {target_cnt}')
                if min_len > end - start + 1:
                    min_start = start
                    min_end = end
                    min_len = end - start + 1
                cnt_map[cur_start_idx] -= 1
                start += 1
                cnt -= 1
            # print(f'cnt_map: {cnt_map},\nneeded : {needed_letter}')
            end += 1

        return s[min_start : min_end + 1] if min_len != s_len + 1 else ""


# @lc code=end

s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "a"))
print(s.minWindow("a", "aa"))
print(s.minWindow("bba", "ab"))
print(s.minWindow("bbaac", "aba"))
