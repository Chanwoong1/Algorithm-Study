# https://www.acmicpc.net/problem/1183

lst = []
N = int(input())
for i in range(N) :
    a, b = map(int, input().split())
    lst.append(a - b)

lst.sort()
if (N % 2 == 1) :
    print(1)
else :
    print(lst[N // 2] - lst[N // 2 - 1] + 1)