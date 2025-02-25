num_of_case = int(input())


def solve(n: int, case: list):
    case = sorted(case)
    repeat = 0
    target = case[0]
    for i in range(0, len(case)):
        if target == case[i]:
            repeat += 1
            if repeat > 2:
                cnt = 0
                while cnt + i < len(case) and case[cnt + i] == target:
                    case[cnt + i] += 1
                    cnt += 1
                target = case[i]
                repeat = 1
        else:
            if repeat < 2: 
                return False
            target = case[i]
            repeat = 1
    return True
        
             


for i in range(0, num_of_case):
    n = int(input())
    case = list(map(int, input().split(' ')))
    if solve(n, case):
        print('Yes')
    else:
        print('No')