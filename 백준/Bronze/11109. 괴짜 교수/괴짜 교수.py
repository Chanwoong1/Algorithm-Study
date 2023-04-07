for _ in range(int(input())) :
    d, n, s, p = map(int, input().split())
    if d + (n * p) < n * s : print("parallelize")
    elif d + (n * p) == n * s : print("does not matter")
    else : print("do not parallelize")
