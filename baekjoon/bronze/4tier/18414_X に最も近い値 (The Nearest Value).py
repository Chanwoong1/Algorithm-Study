# https://www.acmicpc.net/problem/18414

X, L, R = map(int, input().split())
if X < L :
    print(abs(L))
elif X > R :
    print(abs(R))
else :
    print(X)