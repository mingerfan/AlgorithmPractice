t = int(input())
for i in range(t):
    n, k, p = map(int, input().split())
    lower_bound = n * (-p)
    upper_bound = n * p
    if k < lower_bound or k > upper_bound:
        print(-1)
    else:
        print(abs(k) // p + (0 if k % p == 0 else 1))