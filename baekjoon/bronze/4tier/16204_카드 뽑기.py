# https://www.acmicpc.net/problem/16204

N, M, K = map(int, input().split())
mo = M
mx = N - M
ko = K
kx = N - K
print(min(mo, ko) + min(mx, kx))