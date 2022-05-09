# https://www.acmicpc.net/problem/10103

c, s = 100, 100
for i in range(int(input())) :
    cs, ss = list(map(int, input().split()))
    if cs > ss :
        s -= cs
    elif cs < ss :
        c -= ss
print(c)
print(s)