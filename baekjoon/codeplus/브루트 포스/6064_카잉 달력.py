# https://www.acmicpc.net/problem/6064

for _ in range(int(input())) :
    M, N, x, y = list(map(int, input().split()))
    year = 1
    while 1 :
        if year % M == x and year % N == y :
            print(year)
            break
        if year == M * N + 1 :
            print(-1)
            break
        year += 1
