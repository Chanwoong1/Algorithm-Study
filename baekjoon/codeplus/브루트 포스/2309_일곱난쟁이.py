# https://www.acmicpc.net/problem/2309

from itertools import combinations

lst = []
for _ in range(9) :
    lst.append(int(input()))
tmp = sum(lst) - 100
for i in combinations(lst, 2) :
    if tmp == sum(i) :
        a = i[0]
        b = i[1]
        break
lst.remove(a)
lst.remove(b)
lst.sort()
for i in lst :
    print(i)