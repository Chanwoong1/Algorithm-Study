# https://www.acmicpc.net/problem/15051

A1 = int(input())
A2 = int(input())
A3 = int(input())
# 1F
f1 = A2 * 2 + A3 * 4
# 2F
f2 = A1 * 2 + A3 * 2
# 3F
f3 = A1 * 4 + A2 * 2
print(min(f1, f2, f3))