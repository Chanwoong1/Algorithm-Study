# https://www.acmicpc.net/problem/15655

from itertools import combinations
N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()
for i in combinations(lst, M) :
    tmp = [str(j) for j in i]
    print(' '.join(tmp))