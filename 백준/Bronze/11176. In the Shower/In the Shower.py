for _ in range(int(input())) :
    cnt = 0
    E, N = map(int, input().split())
    for _ in range(N) :
        if int(input()) > E : cnt += 1
    print(cnt)
