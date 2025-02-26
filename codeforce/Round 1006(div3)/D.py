t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    cur_cost = 0
    max_cost = 0
    max_cost_start = 0
    max_cost_end = 0
    for start in range(0, n):
        cur_cost = 0
        for end in range(start + 1, n):
            if arr[end] < arr[start]:
                cur_cost += 1
            elif arr[end] > arr[start]:
                cur_cost -= 1
            if cur_cost > max_cost:
                max_cost = cur_cost
                max_cost_start = start
                max_cost_end = end
    print(f'{max_cost_start + 1} {max_cost_end + 1}')
            
