# https://www.acmicpc.net/problem/6603

from itertools import combinations

lst = list(map(int, input().split()))
while 1 :
    lst.pop(0)
    for i in list(combinations(lst, 6)) :
        tmp = [str(j) for j in i]
        print(' '.join(tmp))
    lst = list(map(int, input().split()))
    if lst[0] == 0 :
        break
    print()