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