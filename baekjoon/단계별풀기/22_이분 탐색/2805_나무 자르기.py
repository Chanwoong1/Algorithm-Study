# https://www.acmicpc.net/problem/2805

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
le = 1
ri = max(lst) 
while le <= ri : 
    mid = (le + ri) // 2 
    total = 0
    for i in lst : 
        if i >= mid :
            total += (i - mid) 
    if total >= M : 
        le = mid + 1 
    else : 
        ri = mid - 1 
print(ri)