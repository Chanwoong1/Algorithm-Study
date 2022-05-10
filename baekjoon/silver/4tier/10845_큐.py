# https://www.acmicpc.net/problem/10845

import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())) :
    tmp = list(input().split())
    if tmp[0] == 'push' :
        lst.append(tmp[1])
    elif tmp[0] == 'pop' :
        if len(lst) == 0 :
            print(-1)
        else :
            print(lst.pop(0))
    elif tmp[0] == 'size' :
        print(len(lst))
    elif tmp[0] == 'empty' :
        if len(lst) == 0 :
            print(1)
        else :
            print(0)
    elif tmp[0] == 'front' :
        if len(lst) == 0 :
            print(-1)
        else :
            print(lst[0])
    else :
        if len(lst) == 0 :
            print(-1)
        else :
            print(lst[-1])