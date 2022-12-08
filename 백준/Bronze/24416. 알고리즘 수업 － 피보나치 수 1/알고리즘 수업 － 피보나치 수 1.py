def fibo(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        return (fibo(n - 1) + fibo(n - 2))

def fibonacci(n) :
    dp[1] = dp[2] = 1
    if n > 2 :
        for i in range(3, n) :
            dp[i] = dp[i - 1] + dp[i - 2]
    
N = int(input())
dp = [0] * N
fibonacci(N)
print(fibo(N), len(dp) - 2)
