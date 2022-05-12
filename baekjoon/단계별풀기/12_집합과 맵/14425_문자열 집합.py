# https://www.acmicpc.net/problem/14425

N, M = list(map(int, input().split()))

S = []
for _ in range(N) :
    S.append(input())

answer = 0
for _ in range(M) :
    if input() in S :
        answer += 1
print(answer)