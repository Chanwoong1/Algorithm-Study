N, R = map(int, input().split())
dp = [1] + [i for i in range(1, 1000001)]
dp2 = [1] * 1000001
for i in range(1, 1000001) :
    dp2[i] = dp[i] * dp2[i - 1] % 1000000007
print(int(dp2[N] / (dp2[N - R] * dp2[R])))