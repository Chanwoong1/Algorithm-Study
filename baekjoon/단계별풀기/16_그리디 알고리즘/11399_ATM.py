# https://www.acmicpc.net/problem/11399

N = int(input())
lst = sorted(list(map(int, input().split())))   # 정렬만 해주면 끝
time = 0
for i in range(N) :
    time += sum(lst[ : i + 1])
print(time)