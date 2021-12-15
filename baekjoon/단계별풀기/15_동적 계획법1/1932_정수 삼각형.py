# https://www.acmicpc.net/problem/1932

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            lst[i][j] = lst[i][j] + lst[i - 1][j]
        elif i == j:
            lst[i][j] = lst[i][j] + lst[i - 1][j - 1]
        else:
            lst[i][j] = max(lst[i][j]+lst[i - 1][j],
                               lst[i][j]+lst[i - 1][j - 1])
print(max(lst[n - 1]))
