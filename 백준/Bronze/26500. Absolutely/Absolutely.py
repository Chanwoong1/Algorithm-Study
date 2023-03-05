for _ in range(int(input())) :
    a, b = map(float, input().split())
    print("{:.1f}".format(abs(a - b)))
