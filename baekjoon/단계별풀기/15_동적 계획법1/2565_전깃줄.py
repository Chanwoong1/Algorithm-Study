# https://www.acmicpc.net/problem/2565

# N = int(input())
# lst = []
# for i in range(N) :
#     tmp = list(map(int, input().split()))
#     tmp.append(abs(tmp[0] - tmp[1]))
#     lst.append(tmp)
# lst.sort(key = lambda x : x[2], reverse = True)
# result = []
# for i in lst :
#     result.append(i)
#     j = len(result) - 1
#     for k in range(0, j) :
#         if ((result[k][0] > result[j][0]) and (result[k][1] > result[j][1])) or \
#             ((result[k][0] < result[j][0]) and (result[k][1] < result[j][1])) :
#             result.pop(k)
#             break
#     print(result)
# print(result)
# print(len(lst) - len(result))

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort()

dp = [1]*N
for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
print(N-max(dp))