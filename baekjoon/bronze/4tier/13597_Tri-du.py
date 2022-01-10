# https://www.acmicpc.net/problem/13597

lst = list(map(int, input().split()))
if lst[0] == lst[1] :
    print(lst[0])
else :
    print(max(lst))