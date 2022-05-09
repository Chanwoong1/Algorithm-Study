# https://www.acmicpc.net/problem/10214

for _ in range(int(input())) :
    ys, ks = 0, 0
    for _ in range(9) :
        y, k = list(map(int, input().split()))
        ys += y
        ks += k
    if ys > ks :
        print("Yonsei")
    elif ks > ys :
        print("Korea")
    else :
        print("Draw")