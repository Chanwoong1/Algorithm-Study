# https://www.acmicpc.net/problem/2164

from collections import deque
n = int(input())
q = deque([i for i in range(1, n + 1)])
while len(q) > 1 :
    q.popleft()
    q.append(q.popleft())
print(q[0])

# popleft : queue에서 사용하는 함수로, 일반 list에서 pop(0)과 동일한 동작을 한다.
# 그러나 시간복잡도 상으로 pop(0)은 O(n)의 시간이 걸리는데,
# popleft()는 O(1)의 시간이 걸린다.
# index를 사용하여 바로 값을 찾는것. 그래서 쓰는것같다.