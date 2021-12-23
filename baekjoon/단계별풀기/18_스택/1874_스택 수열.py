# https://www.acmicpc.net/problem/1874

n = int(input())
stack = []
answer = []
i = 1
result = True
for _ in range(n) :
    x = int(input())
    while i <= x :
        stack.append(i)
        answer.append('+')
        i += 1
    
    if stack[-1] == x :
        stack.pop()
        answer.append('-')
    else :
        result = False

if result == False :
    print('NO')
else :
    for i in answer :
        print(i)
