# https://www.acmicpc.net/problem/11549

T = int(input())
lst = list(map(int, input().split()))
answer = 0
for i in lst :
    if T == i :
        answer += 1
print(answer)