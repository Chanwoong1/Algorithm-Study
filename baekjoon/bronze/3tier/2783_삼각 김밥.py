# https://www.acmicpc.net/problem/2783

X, Y = map(int, input().split())
tmp = X / Y
N = int(input())
for _ in range(N) :
    x, y = map(int, input().split())
    if tmp > x / y :
        tmp = x / y
print(tmp * 1000)