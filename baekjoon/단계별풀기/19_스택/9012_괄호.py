# https://www.acmicpc.net/problem/9012

''' 예제만 맞음
for _ in range(int(input())) :
    vps = list(input())
    x = 0
    y = 0
    for i in vps :
        if i == '(' :
            x += 1
        else :
            y += 1

    if x != y :
        print('NO')
    else :
        print('YES')
'''

# 수정 - 스택 구현
for _ in range(int(input())) :
    vps = list(input())
    stack = []
    answer = 'YES'
    for i in vps :
        if len(stack) == 0 and i == ')' :
            answer = 'NO'
        elif len(stack) != 0 and i == ')' :
            stack.pop()
        else :
            stack.append(1)
    if len(stack) != 0 :
        print('NO')
    else :
        print(answer)
        


