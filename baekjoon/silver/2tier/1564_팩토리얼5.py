# https://www.acmicpc.net/problem/1564

N = int(input())
answer = 1
for i in range(1, N + 1) :
    answer *= i
    while answer % 10 == 0 :
        answer = answer // 10
    answer = answer % 100000000000000000
print(str(answer)[-5:])