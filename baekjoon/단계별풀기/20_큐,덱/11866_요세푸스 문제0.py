# https://www.acmicpc.net/problem/11866

from collections import deque
N, M = list(map(int, input().split()))
d = deque([i for i in range(1, N + 1)])
answer = []
while len(d) > 1 :
    for _ in range(M - 1) :
        d.append(d.popleft())
    answer.append(d.popleft())
answer.append(d.popleft())
print("<", end = '')
for i in range(len(answer) - 1) :
    print(answer[i], end = ', ')
print(answer[-1], end = '')
print('>')