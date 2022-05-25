# https://www.acmicpc.net/problem/1380

scenario = 0

answer = []
while 1 :
    N = int(input())
    if N == 0 :
        break
    scenario += 1
    name = ['0']
    ring = ['0']
    ret = [0] * (N + 1)
    for _ in range(N) :
        a, b = input().split()
        name.append(a)
        ring.append(b)
    for _ in range(2 * N - 1) :
        a, b = list(input().split())
        ret[int(a)] += 1
    for i in range(1, N + 1) :
        if ret[i] != 2 :
            answer.append([scenario, name[i], ring[i]])
for i in answer :
    print(*i)