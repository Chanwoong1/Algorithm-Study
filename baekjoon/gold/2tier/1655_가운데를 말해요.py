# https://www.acmicpc.net/problem/1655

import sys
import heapq
input = sys.stdin.readline
lst_max, lst_min = [], []
for _ in range(int(input())) :
    if len(lst_max) == len(lst_min) :
        heapq.heappush(lst_max, -int(input()))
    else :
        heapq.heappush(lst_min, int(input()))
    
    if len(lst_max) >= 1 and len(lst_min) >= 1 and lst_max[0] * -1 > lst_min[0] :
        max_value = heapq.heappop(lst_max) * -1
        min_value = heapq.heappop(lst_min)

        heapq.heappush(lst_max, min_value * -1)
        heapq.heappush(lst_min, max_value)
    
    print(lst_max[0] * -1)