# https://www.acmicpc.net/problem/11660

# N, M = list(map(int, input().split()))
# lst = [[0 for _ in range(N + 1)]]
# last_lst = [0 for _ in range(N + 1)]
# for _ in range(N) :
#     tmp = list(map(int, input().split()))
#     tmp_sum = 0
#     tmp_lst = [0]
#     for i in range(1, len(tmp) + 1) :
#         tmp_sum += tmp[i - 1] + last_lst[i] - last_lst[i - 1]
#         tmp_lst.append(tmp_sum)
#     last_lst = tmp_lst
#     lst.append(tmp_lst)
# for _ in range(M) :
#     x1, y1, x2, y2 = list(map(int, input().split()))
#     answer = lst[x2][y2] - lst[x2][y1 - 1] - lst[x1 - 1][y2] + lst[x1 - 1][y1 - 1]
#     print(answer)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
s = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + s[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x1 - 1][y2] + dp[x2][y1 - 1] - dp[x1 - 1][y1 - 1]))