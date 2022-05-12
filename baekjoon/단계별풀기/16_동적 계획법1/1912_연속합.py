# https://www.acmicpc.net/problem/1912


# 시간 초과 - 2중 for문 때문에 그런것같다
n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
_lst = [i for i in lst if i >= 0]
if len(_lst) == 0 :
    print(max(lst))
else :
    for i in range(n) :
        dp_j = [0] * n
        for j in range(i, n) :
            dp_j[j - 1] = sum(lst[i : j])
        dp_j[j] = lst[-1]
        dp[i] = max(dp_j)
    print(max(dp))

# 수정
n = int(input())
lst = list(map(int, input().split()))

dp = [0] * n
dp[0] = lst[0]

for i in range(1, n) :
    dp[i] = max(lst[i], dp[i - 1] + lst[i])
print(max(dp))