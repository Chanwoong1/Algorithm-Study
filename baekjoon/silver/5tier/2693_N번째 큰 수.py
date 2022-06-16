# https://www.acmicpc.net/problem/2693

N = int(input())
for _ in range(N) :
    lst = sorted(list(map(int, input().split())))
    print(lst[7])

# 줄이면
for _ in range(int(input())) :
    print(sorted(list(map(int, input().split())))[7])