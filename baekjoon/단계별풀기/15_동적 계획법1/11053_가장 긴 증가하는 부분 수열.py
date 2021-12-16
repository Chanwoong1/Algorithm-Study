# https://www.acmicpc.net/problem/11053

N = int(input())
lst = list(map(int, input().split()))

dp = [lst[0]]
for i in range(1, N) :
    if dp[-1] < lst[i] :
        dp.append(lst[i])
    else :
        idx = 0
        for j in range(len(dp)) :
            if dp[j] < lst[i] :
                idx += 1
            else :
                dp[idx] = lst[i]
                break
print(len(dp))

