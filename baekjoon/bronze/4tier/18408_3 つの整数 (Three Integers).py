# https://www.acmicpc.net/problem/18408

lst = list(map(int, input().split()))
if sum(lst) < 5 :
    print(1)
else :
    print(2)