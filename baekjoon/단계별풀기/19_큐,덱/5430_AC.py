# https://www.acmicpc.net/problem/5430

import sys
from collections import deque
tc = int(input())
for _ in range(tc) :
    func = input()
    func = func.replace('RR', '')
    func = list(func)
    num = int(input())
    case = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    
    rev, front, back = 0, 0, len(case)-1
    flag = 0
    if num == 0:
        case = []
        front = 0
        back = 0

    for j in func:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(case) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    case.popleft()
                else:
                    case.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(case) + "]")
        else:
            case.reverse()
            print("[" + ",".join(case) + "]")
