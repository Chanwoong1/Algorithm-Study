# https://www.acmicpc.net/problem/13136

R, C, N = map(int, input().split())
if R % N == 0 :
    R = R // N
else :
    R = R // N + 1
if C % N == 0 :
    C = C // N
else :
    C = C // N + 1
print(R * C)