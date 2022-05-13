# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
sum_lst = [0]
tmp = 0
for i in lst :
    tmp += i
    sum_lst.append(tmp)

for _ in range(M) :
    start, end = list(map(int, input().split()))
    print(sum_lst[end] - sum_lst[start - 1])