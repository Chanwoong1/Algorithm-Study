# https://www.acmicpc.net/problem/10816

from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
lst = Counter(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))
for i in M_lst :
    if lst[i] :
        print(lst[i], end = ' ')
    else :
        print(0, end = ' ')