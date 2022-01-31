# https://www.acmicpc.net/problem/2576

lst = []
for _ in range(7) :
    n = int(input())
    if n % 2 != 0 :
        lst.append(n)
if len(lst) == 0 :
    print(-1)
else :
    print(sum(lst))
    print(min(lst))