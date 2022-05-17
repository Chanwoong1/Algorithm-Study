# https://www.acmicpc.net/problem/1476

E, S, M = list(map(int, input().split()))
i = 1
while 1 :
    if i % 15 == E % 15 and i % 28 == S % 28 and i % 19 == M % 19 :
        print(i)
        break
    i += 1