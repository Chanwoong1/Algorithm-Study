# https://www.acmicpc.net/problem/2485

lst = []
for _ in range(int(input())) :
    lst.append(int(input()))

dt = []
for i in range(1, len(lst)) :
    dt.append(lst[i] - lst[i - 1])

i = 1
while i < min(dt) :
    

answer = 0
tree = lst[0]
while tree <= max(lst) :
    if tree not in lst :
        answer += 1
    tree += min(dt)
print(answer)