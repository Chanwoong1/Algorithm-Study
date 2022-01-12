# https://www.acmicpc.net/problem/21354

A, P = map(int, input().split())
A *= 7
P *= 13
if A > P :
    print('Axel')
elif A < P :
    print('Petra')
else :
    print('lika')