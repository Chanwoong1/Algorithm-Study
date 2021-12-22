# https://www.acmicpc.net/problem/1934

N = int(input())

for _ in range(N) :
    A, B = sorted(list(map(int, input().split())))
    a, b = A, B
    while A != 0 :
        B = B % A
        A, B = B, A
    max_ = B
    print(a * b // B)