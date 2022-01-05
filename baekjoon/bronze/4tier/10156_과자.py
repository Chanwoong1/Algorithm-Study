# https://www.acmicpc.net/problem/10156

K, N, M = map(int, input().split())
result = M - K * N
if result < 0 :
    print(abs(result))
else :
    print(0)