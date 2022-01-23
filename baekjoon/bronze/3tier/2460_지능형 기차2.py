# https://www.acmicpc.net/problem/2460

answer = 0
lst = []
for _ in range(10) :
    a, b = map(int, input().split())
    answer += b - a
    lst.append(answer)
print(max(lst))