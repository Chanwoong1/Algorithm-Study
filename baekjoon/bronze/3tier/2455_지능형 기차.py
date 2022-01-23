# https://www.acmicpc.net/problem/2455

answer = 0
lst = []
for _ in range(4) :
    a, b = map(int, input().split())
    answer += b - a
    lst.append(answer)
print(max(lst))