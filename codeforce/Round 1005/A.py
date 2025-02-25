n = int(input())

for n in range(n):
    num_len = int(input())
    s = input()
    # s likes '1011010101'
    cnt = 0
    target = '0'
    for i in s:
        if i == '0' and target == '1':
            cnt += 1
            target = '0'
        elif i == '1' and target == '0':
            cnt += 1
            target = '1'
    print(cnt)