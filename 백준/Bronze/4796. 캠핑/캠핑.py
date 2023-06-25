t = 1
while 1:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    ans = V // P * L + (V % P if V % P < L else L)
    print("Case {}: {}".format(t, ans))
    t += 1
