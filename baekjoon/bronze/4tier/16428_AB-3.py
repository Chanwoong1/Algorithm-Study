# https://www.acmicpc.net/problem/16428

A, B = map(int, input().split())
a, b = A // B, A % B
if A != 0 and b < 0:
    a, b = a + 1, b - B
print(a)
print(b)