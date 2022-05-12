# https://www.acmicpc.net/problem/10866

from collections import deque
import sys
deq = deque([])
for _ in range(int(input())) :
    x = sys.stdin.readline().split()
    if x[0] == 'push_front' :
        if not deq :
            deq.append(x[1])
        else :
            deq.insert(0, x[1])
    elif x[0] == 'push_back' :
        deq.append(x[1])
    elif x[0] == 'pop_front' :
        if not deq :
            print(-1)
        else :
            print(deq.popleft())
    elif x[0] == 'pop_back' :
        if not deq :
            print(-1)
        else :
            print(deq.pop())
    elif x[0] == 'size' :
        print(len(deq))
    elif x[0] == 'empty' :
        if not deq :
            print(1)
        else :
            print(0)
    elif x[0] == 'front' :
        if not deq :
            print(-1)
        else :
            print(deq[0])
    else :
        if not deq :
            print(-1)
        else :
            print(deq[-1])
