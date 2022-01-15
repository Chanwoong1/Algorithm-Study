# https://www.acmicpc.net/problem/1547

M = int(input())

ball = 1
for _ in range(M) :
    x, y = map(int, input().split())
    if x == y :
        pass
    else :
        if x == ball :
            ball = y
        elif y == ball :
            ball = x
print(ball)
