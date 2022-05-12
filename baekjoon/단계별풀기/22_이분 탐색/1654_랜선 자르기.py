# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]
le = 1
ri = max(lst) 
while le <= ri : 
    mid = (le + ri) // 2 
    total = 0 
    for i in lst : 
        total += (i // mid) 
    if total < N : 
        ri = mid - 1 
    else : 
        le = mid + 1 
print(ri)