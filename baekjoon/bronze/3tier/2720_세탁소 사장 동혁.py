# https://www.acmicpc.net/problem/2720

T = int(input())
for _ in range(T) :
    C = int(input())
    Q = 0
    D = 0
    N = 0
    P = 0
    if C >= 25 :
        Q = C // 25
        C = C % 25

    if C >= 10 :
        D = C // 10
        C = C % 10

    if C >= 5 :
        N = C // 5
        C = C % 5

    if C >= 1 :
        P = C // 1

    print(Q, D, N, P)