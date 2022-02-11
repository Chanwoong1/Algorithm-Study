# https://www.acmicpc.net/problem/2965

a, b, c = map(int, input().split())
d = max(b - a, c - b)
print(d - 1)