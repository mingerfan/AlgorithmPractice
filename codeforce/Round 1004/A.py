n = int(input())

for i in range(0, n):
    x, y = tuple(map(int, input().split(' ')))
    if y == x + 1 or (y < x and (x - y + 1) % 9 == 0):
        print('Yes')
    else:
        print('No')