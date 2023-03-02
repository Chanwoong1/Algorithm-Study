dp = [0] * 1000001
for i in range(1, 1000001) :
    dp[i] += dp[i - 1] + i
while True :
    n = int(input())
    if n == 0 : break
    print(dp[n])
