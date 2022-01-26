# https://www.acmicpc.net/problem/2501

N, K = map(int, input().split())
n = 1
while 1 :
    if N % n == 0 :
        K -= 1

    if K == 0 :
        print(n)
        break

    if N < n :
        print(0)
        break
        
    n += 1