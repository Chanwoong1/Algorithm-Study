# https://www.acmicpc.net/problem/1059

L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.append(0)
S.sort()
for i in range(len(S) - 1) :
    if S[i] == n or S[i + 1] == n :
        print(0)
        break
    elif S[i] < n and n < S[i + 1] :
        print((n - S[i]) * (S[i + 1] - n) - 1)
        break

