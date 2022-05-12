# https://www.acmicpc.net/problem/1920

import sys
input = sys.stdin.readline
N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
tmp = list(map(int, input().split()))

def binary(l, N, start, end) :
    if start > end :
        return 0
    m = (start+end) // 2
    if l == N[m] :
        return 1
    elif l < N[m] :
        return binary(l, N, start, m-1)
    else :
        return binary(l, N, m+1, end)

for l in tmp :
    start = 0
    end = len(lst) - 1
    print(binary(l, lst, start, end))