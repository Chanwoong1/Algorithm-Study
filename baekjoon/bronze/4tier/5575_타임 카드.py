# https://www.acmicpc.net/problem/5575

lst = [list(map(int, input().split())) for _ in range(3)]
for i in range(3) :
    h = lst[i][3] - lst[i][0]
    m = lst[i][4] - lst[i][1]
    s = lst[i][5] - lst[i][2]
    if s < 0 :
        s += 60
        m -= 1
    if m < 0 :
        m += 60
        h -= 1
    print(h, m, s)
