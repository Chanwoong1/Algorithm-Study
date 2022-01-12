# https://www.acmicpc.net/problem/24083

A = int(input())
B = int(input())
H = A + B
if H > 12 :
    h = H // 12
    H = H - 12 * h
    if H == 0 :
        print(12)
    else :
        print(H)
else :
    print(H)