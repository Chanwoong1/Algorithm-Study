# https://www.acmicpc.net/problem/4101

while (1) :
    a, b = list(map(int, input().split()))
    if a == 0 & b == 0 :
        break
    if a > b :
        print("Yes")
    else :
        print("No")