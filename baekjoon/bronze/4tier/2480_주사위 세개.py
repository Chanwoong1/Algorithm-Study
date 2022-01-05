# https://www.acmicpc.net/problem/2480

A, B, C = map(int, input().split())
if A == B and B == C :
    print(10000 + 1000 * A)
elif A == B :
    print(1000 + 100 * A)
elif A == C :
    print(1000 + 100 * A)
elif B == C :
    print(1000 + 100 * B)
else :
    print(100 * max(A, B, C))