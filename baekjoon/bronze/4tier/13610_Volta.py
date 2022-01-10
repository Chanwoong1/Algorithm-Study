# https://www.acmicpc.net/problem/13610

X, Y = map(int, input().split())
if X * 2 <= Y :
    print(2)
else :
    if Y % (Y - X) == 0 :
        print(Y // (Y - X))
    else :
        print(Y // (Y - X) + 1)