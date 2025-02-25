n = int(input())

for i in range(n):
    nums_len = int(input())
    nums_list= list(map(int, input().split(' ')))
    # 统计每一个数字的出现次数
    nums_dict = {}
    for num in nums_list:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    # 滑动窗口计算最长子串，子串中的数字在nums_dict中出现次数不超过1次
    # 统计最长的left和right
    left = 0
    right = 0
    max_len = 0
    max_left = 0
    max_right = 0
    while right < nums_len:
        # print(max_len)
        if nums_dict[nums_list[right]] > 1:
            # 整个序列放弃，从下一个开始
            if max_len < right - left:
                max_len = right - left
                max_left = left
                max_right = right - 1
            right += 1
            left = right
        else:
            right += 1
    if max_len < right - left:
        max_len = right - left
        max_left = left
        max_right = right - 1
    if max_len > 0:
        print(f'{max_left + 1} {max_right + 1}')
    else:
        print(0)