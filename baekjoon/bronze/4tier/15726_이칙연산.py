# https://www.acmicpc.net/problem/15726

A, B, C = map(int, input().split())
print(int(max(A * B / C, A / B * C)))