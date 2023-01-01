from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0 for _ in range(w - 1)])
bridge.append(trucks.popleft())
time = 1
while trucks :
    if sum(bridge) - bridge[0] + trucks[0] <= L :
        bridge.popleft()
        bridge.append(trucks.popleft())
    else :
        bridge.popleft()
        bridge.append(0)
    time += 1
while sum(bridge) != 0 :
    bridge.popleft()
    time += 1
print(time)