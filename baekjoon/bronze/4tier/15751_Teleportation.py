# https://www.acmicpc.net/problem/15751

a, b, x, y = map(int, input().split())
r1 = abs(b - a)
r2 = abs(x - a) + abs(y - b)
r3 = abs(y - a) + abs(x - b)
print(min(r1, r2, r3))