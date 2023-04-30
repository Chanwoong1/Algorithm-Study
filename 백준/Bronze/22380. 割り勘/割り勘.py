while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    lst = [*map(int, input().split())]
    ans = 0
    for i in lst:
        ans += i if i < M // N else M // N
    print(ans)
