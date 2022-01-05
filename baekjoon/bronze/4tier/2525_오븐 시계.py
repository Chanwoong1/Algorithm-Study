# https://www.acmicpc.net/problem/2525

A, B = map(int, input().split())
C = int(input())
tmp = B + C
if tmp >= 60 :
    A += tmp // 60
    tmp %= 60
if A >= 24 :
    A -= 24
print(A, tmp)