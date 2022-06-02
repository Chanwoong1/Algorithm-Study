# https://www.acmicpc.net/problem/1205

N, taesu, P = map(int, input().split())
if N == 0 :
    print(1)
else :
    rank = list(map(int, input().split()))
    if N == P and rank[-1] >= taesu :
        print(-1)
    else :
        res = N + 1
        for i in range(N) :
            if rank[i] <= taesu :
                res = i + 1
                break
        print(res)