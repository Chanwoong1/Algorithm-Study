# https://www.acmicpc.net/problem/10973

N = int(input())
lst = list(map(int, input().split()))

for i in range(N - 1, 0, -1) :
    if lst[i - 1] > lst[i] :
        for j in range(N - 1, 0, -1) :
            if lst[i - 1] > lst[j] :
                lst[i - 1], lst[j] = lst[j], lst[i - 1]
                lst = lst[:i] + sorted(lst[i:], reverse = True)
                print(*lst)
                exit()

print(-1)