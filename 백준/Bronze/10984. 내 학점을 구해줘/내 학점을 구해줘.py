for _ in range(int(input())) :
    n = int(input())
    grade = 0
    total = 0
    for _ in range(n) :
        a, b = map(float, input().split())
        grade += b * a
        total += a
    print(int(total), round(grade / total, 1))
