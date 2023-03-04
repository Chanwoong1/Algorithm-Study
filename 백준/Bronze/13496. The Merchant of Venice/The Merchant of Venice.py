idx = 1
for _ in range(int(input())) :
    n, s, d = map(int, input().split())
    ans = 0
    for _ in range(n) :
        di, vi = map(int, input().split())
        if (di / s <= d) : ans += vi
    print("Data Set {:d}:".format(idx))
    print(ans)
    print()
    idx += 1
