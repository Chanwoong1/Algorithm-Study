# https://www.acmicpc.net/problem/15474

N, A, B, C, D = map(int, input().split())
if N % A == 0 :
    A = N // A
else :
    A = N // A + 1
if N % C == 0 :
    C = N // C
else :
    C = N // C + 1
print(min(A * B, C * D))