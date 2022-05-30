# https://www.acmicpc.net/problem/1206

N = int(input())
lst = [float(input()) for _ in range(N)]
answer = 1
while 1 :
    tmp = [1 for i in lst if i * answer % 1 == 0]
    if sum(tmp) == N :
        break
    answer += 1
print(answer)