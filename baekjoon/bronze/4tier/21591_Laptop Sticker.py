# https://www.acmicpc.net/problem/21591

wc, hc, ws, hs = map(int, input().split())
if (wc - ws) / 2 >= 1 and (hc - hs) / 2 >= 1 :
    print(1)
else :
    print(0)