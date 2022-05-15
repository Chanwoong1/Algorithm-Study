# https://www.acmicpc.net/problem/11286

import heapq
import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())) :
    n = int(input())
    if n != 0 :
        heapq.heappush(lst, (abs(n), n))
    else :
        try :
            print(heapq.heappop(lst)[1])
        except :
            print(0)