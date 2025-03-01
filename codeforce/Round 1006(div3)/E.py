import math

t = int(input())

def solve(k):
    axis_x, axis_y = 0, 0
    res_list = []
    first = True
    while k > 0:
        if k == 1 and not first:
            res_list.append((axis_x, axis_y))
            break
        elif k == 1 and first:
            res_list.append((axis_x, axis_y))
            axis_x += 1
            res_list.append((axis_x, axis_y))
            break
        try_n = math.floor(math.sqrt(2 * k))
        last_n = try_n
        while try_n - (try_n * try_n - try_n) // 2 > 0:
            last_n = try_n
            try_n += 1
        try_n = last_n 
        for _ in range(try_n):
            res_list.append((axis_x, axis_y))
            axis_x += 1
        axis_y += 1
        axis_x -= 1
        k -= (try_n * try_n - try_n) // 2 + (1 if not first else 0)
        first = False
    return res_list

for _ in range(t):
    k = int(input())

    res = solve(k)

    print(len(res))
    for x, y in res:
        print(f'{x} {y}')

# for i in range(99001, 100001):
#     res = solve(i)
#     if len(res) > 500:
#         print(f'{i}: {len(res)}')