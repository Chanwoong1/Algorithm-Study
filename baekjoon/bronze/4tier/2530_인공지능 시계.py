# https://www.acmicpc.net/problem/2530

A, B, C = map(int, input().split())
D = int(input())
tmp = C + D
if tmp >= 3600 :
    A += tmp // 3600
    tmp %= 3600
if tmp >= 60 :
    B += tmp // 60
    tmp %= 60
if B >= 60 :
    m = (B // 60)
    B -= 60 * m
    A += 1 * m
if A >= 24 :
    h = (A // 24)
    A -= 24 * h
print(A, B, tmp)