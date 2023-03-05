for _ in range(int(input())) :
    a, b = map(int, input().split())
    print(a, b)
    if a > 1 : print(b + (b - 2) * (a - 1))
    else : print(b)
