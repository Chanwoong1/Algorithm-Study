# https://www.acmicpc.net/problem/2010

import sys
input = sys.stdin.readline
N = int(input())
res = 0
for _ in range(N) :
    res += int(input())
print(res - N + 1)