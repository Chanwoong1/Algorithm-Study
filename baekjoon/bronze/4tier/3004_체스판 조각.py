# https://www.acmicpc.net/problem/3004

N = int(input())
if N == 1 :
    print(2)
else :
    if N % 2 == 0 :
        print((N // 2 + 1) * (N // 2 + 1))
    else :
        print((N // 2 + 1) * (N // 2 + 2))