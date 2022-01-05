# https://www.acmicpc.net/problem/10797

N = int(input())
lst = list(map(int, input().split()))
answer = 0
for i in lst :
    if i == N :
        answer += 1
print(answer)