# https://www.acmicpc.net/problem/1406

import sys

input = sys.stdin.readline
str = list(input())
str.pop()
stack = []
for _ in range(int(input())) :
    tmp = list(input().split())
    if tmp[0] == 'D' :
        if stack :
            str.append(stack.pop())
    elif tmp[0] == 'L' :
        if str :
            stack.append(str.pop())
    elif tmp[0] == 'B' :
        if str :
            str.pop()
    else :
        str.append(tmp[1])
str.extend(reversed(stack))
print(''.join(str))