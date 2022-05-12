# https://www.acmicpc.net/problem/4949

while 1 :
    x = input()
    if x == '.' :
        break
    
    stack = []
    answer = 'yes'
    for i in x :
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' :
            if not stack or stack[-1] == '[' :
                answer = 'no'
                break
            elif stack[-1] == '(' :
                stack.pop()
        elif i == ']' :
            if not stack or stack[-1] == '(' :
                answer = 'no'
                break
            elif stack[-1] == '[' :
                stack.pop()       
        
    if not stack :
        print(answer)
    else :
        print('no')
