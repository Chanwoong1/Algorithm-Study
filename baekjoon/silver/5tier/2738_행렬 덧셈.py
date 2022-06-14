# https://www.acmicpc.net/problem/2738

N, M = map(int, input().split())
lst = []
for _ in range(N) :
    lst.append(list(map(int, input().split())))
answer = []
for i in lst :
    tmp = list(map(int, input().split()))
    answer.append([i[j] + tmp[j] for j in range(M)])
for i in answer :
    print(*i)