# https://www.acmicpc.net/problem/5063

for _ in range(int(input())) :
    r, e, c = list(map(int, input().split()))
    if r > e - c :
        print("do not advertise")
    elif r == e - c :
        print("does not matter")
    else :
        print("advertise")