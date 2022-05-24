# https://www.acmicpc.net/problem/1094

X = int(input())
lst = [64]
while 1 :
    if X == sum(lst) :
        break
    tmp = lst.pop() // 2
    lst.append(tmp)
    if X > sum(lst) :
        lst.append(tmp)    

print(len(lst))