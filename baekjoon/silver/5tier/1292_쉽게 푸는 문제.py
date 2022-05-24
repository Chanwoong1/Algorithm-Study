# https://www.acmicpc.net/problem/1292

A, B = map(int, input().split())
lst = []
i = 1
while 1 :
    if len(lst) > B :
        break
    tmp = [i] * i
    lst += tmp
    i += 1
print(sum(lst[A - 1 : B]))