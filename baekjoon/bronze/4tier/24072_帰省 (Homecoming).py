# https://www.acmicpc.net/problem/24072

A, B, C = map(int, input().split())
if A <= C and B > C :
    print(1)
else :
    print(0)