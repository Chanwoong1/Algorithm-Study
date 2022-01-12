# https://www.acmicpc.net/problem/22015

A, B, C = map(int, input().split())
print(max(A, B, C) - A + max(A, B, C) - B + max(A, B, C) - C)