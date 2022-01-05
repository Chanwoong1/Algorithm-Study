# https://www.acmicpc.net/problem/11943

A, B = map(int, input().split())
C, D = map(int, input().split())
print(min(A + D, B + C))