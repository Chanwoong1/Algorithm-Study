# https://www.acmicpc.net/problem/2156

N = int(input())
lst = [0] + [int(input()) for _ in range(N)] + [0]

dp = [0] * (len(lst) + 2)
dp[1] = lst[1]
dp[2] = dp[1] + lst[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i], dp[i-1])
print(dp[N])


    # dp = [0] * len(lst)
    # for i in range(len(lst) - 2) :
    #     if i > 1 and dp[i - 2] != 0 and dp[i - 1] != 0 :
    #         dp[i] = 0
    #     elif i > 1 and dp[i - 1] == 0 :
    #         if lst[i] + lst[i + 1] > lst[i + 1] + lst[i + 2] :
    #             dp[i] = lst[i]
    #             dp[i + 1] = lst[i + 1]
    #             dp[i + 2] = 0
    #         else :
    #             dp[i] = 0
    #             dp[i + 1] = lst[i + 1]
    #             dp[i + 2] = lst[i + 2]
    #     else :
    #         if lst[i] + lst[i + 1] > lst[i + 1] + lst[i + 2] :
    #             dp[i] = lst[i]
    #             dp[i + 1] = lst[i + 1]
    #             dp[i + 2] = 0
    #         else :
    #             dp[i] = 0
    #             dp[i + 1] = lst[i + 1]
    #             dp[i + 2] = lst[i + 2]
    #     print(dp)
    # print(sum(dp))


    # tmp0 = 0
    # tmp1 = 0
    # tmp2 = 0
    # for i in range(len(lst)) :
    #     if i % 3 == 0 :
    #         tmp0 += lst[i]
    #     elif i % 3 == 1 :
    #         tmp1 += lst[i]        
    #     else :
    #         tmp2 += lst[i]
    # print(sum(lst) - min(tmp0, tmp1, tmp2))
