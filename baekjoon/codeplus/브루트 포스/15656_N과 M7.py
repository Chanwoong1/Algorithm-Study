# https://www.acmicpc.net/problem/15656

from itertools import permutations
N, M = list(map(int, input().split()))
lst = list(map(int, input().split()))
lst.sort()
for i in permutations(lst, M) :
    tmp = [str(j) for j in i]
    print(' '.join(tmp))