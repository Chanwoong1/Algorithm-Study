# https://www.acmicpc.net/problem/1927

import heapq
import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())) :
    n = int(input())
    if n != 0 :
        heapq.heappush(lst, n)
    else :
        try :
            print(heapq.heappop(lst))
        except :
            print(0)