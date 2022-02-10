# https://www.acmicpc.net/problem/2959

s = list(map(int, input().split()))
s.sort()
print(s[0] * s[2])