# https://www.acmicpc.net/problem/1964

N = int(input())
if N == 1 :
    print(5)
else :
    res = 5
    for i in range(2, N + 1) :
        res += 3 * i + 1
    print(res % 45678)
