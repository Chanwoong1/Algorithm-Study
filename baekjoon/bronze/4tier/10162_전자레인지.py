# https://www.acmicpc.net/problem/10162

T = int(input())
A, B, C = 0, 0, 0
if T >= 300 :
    A = T // 300
    T %= 300
if T >= 60 :
    B = T // 60
    T %= 60
if T % 10 == 0 :
    print(A, B, T // 10)
else :
    print(-1)