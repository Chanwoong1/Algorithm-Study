# https://www.acmicpc.net/problem/10828


import sys
N = int(input())

stack = []
for _ in range(N) :
    rec = sys.stdin.readline()  # 그냥 input()은 시간초과
    if 'push' in rec :
        rec = int(rec.split()[1])
        stack.append(rec)
    
    elif 'pop' in rec :
        if len(stack) == 0 :
            print('-1')
        else :
            print(stack.pop())
    
    elif 'size' in rec :
        print(len(stack))
    
    elif 'empty' in rec :
        if len(stack) == 0 :
            print('1')
        else :
            print('0')
        
    else :
        if len(stack) == 0 :
            print('-1')
        else :
            print(stack[-1])

