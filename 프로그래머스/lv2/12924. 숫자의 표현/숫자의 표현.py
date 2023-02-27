def solution(n):
    answer = 0
    dp = [0] * (n + 1)
    for i in range(1, n + 1) : dp[i] += dp[i - 1] + i
    start, end = 1, 0
    while start <= n :
        if dp[start] - dp[end] < n : start += 1
        elif dp[start] - dp[end] > n : end += 1
        else :
            answer += 1
            end += 1
    return answer