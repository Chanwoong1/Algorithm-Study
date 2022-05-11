# https://www.acmicpc.net/problem/2485

import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())) :
    lst.append(int(input()))

dt = []
for i in range(1, len(lst)) :
    dt.append(lst[i] - lst[i - 1])

def GCDofTwoNumbers(a, b) :
    while b != 0 :
        a, b = b, a % b
    return a

answer = 0
tree = lst[0]
while tree <= max(lst) :
    if tree not in lst :
        answer += 1
    tree += GCDofTwoNumbers(min(dt), max(dt))
print(answer)