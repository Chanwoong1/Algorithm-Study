# https://www.acmicpc.net/problem/8723

lst = list(map(int, input().split()))
if lst[0] == lst[1] and lst[1] == lst[2] :
    print(2)
elif max(lst) ** 2 == (sum(lst) - max(lst) - min(lst)) ** 2 + min(lst) ** 2 :
    print(1)
else :
    print(0)