# https://www.acmicpc.net/problem/19698

N, W, H, L = map(int, input().split())
cows = (W // L) * (H // L)
if cows > N :
    print(N)
else :
    print(cows)