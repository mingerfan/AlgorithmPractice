from functools import reduce
from operator import or_


def solve(n: int, x: int):
    if n == 1:
        return [x]

    values = [0]
    for i in range(1, n - 1):
        if x & i:
            values.append(i)
        else:
            break
    else:
        if x & (n - 1) and reduce(or_, [*values, (n - 1)]) == x:
            values.append(n - 1)
        else:
            values.append(x)
        return values

    values.extend([x] * (n - len(values)))
    return values


def main():
    for _ in range(int(input())):
        result = solve(*map(int, input().split()))
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()