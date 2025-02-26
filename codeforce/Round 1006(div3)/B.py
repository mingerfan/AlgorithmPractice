t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    hypen_count = s.count("-")
    hypen_count_left = hypen_count // 2
    hypen_count_right = hypen_count - hypen_count_left
    dash_count = s.count("_")
    print(hypen_count_left * hypen_count_right * dash_count)
