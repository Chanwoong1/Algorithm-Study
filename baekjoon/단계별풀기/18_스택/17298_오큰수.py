# https://www.acmicpc.net/problem/17298

''' 시간 초과
N = int(input())
lst = list(map(int, input().split()))

answer = []
for i in range(N) :
    a = 0
    for j in range(i, N) :
        if lst[i] < lst[j] :
            answer.append(str(lst[j]))
            a += 1
            break
    if a == 0 :
        answer.append('-1')

print(' '.join(answer))
'''

''' 시간 초과 - 반복문을 두번 이상 쓰면 안되는듯
N = int(input())
lst = list(map(int, input().split()))
answer = []
for i in range(N - 1) :
    tmp = lst[i + 1 :]
    while len(tmp) > 0 :
        temp = tmp.pop(0)
        if lst[i] < temp :
            answer.append(temp)
            break
answer.append(-1)
for i in answer :
    print(i, end = ' ')
'''

N = int(input())
lst = list(map(int, input().split()))
answer = [-1] * N
stack = []

stack.append(0)
for i in range(1, N) :
    while stack and lst[stack[-1]] < lst[i] :
        answer[stack.pop()] = lst[i]
    stack.append(i)

print(*answer)