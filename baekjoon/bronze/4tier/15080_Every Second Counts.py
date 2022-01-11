# https://www.acmicpc.net/problem/15080

lst1 = list(input().split())
lst2 = list(input().split())
h = int(lst2[0]) - int(lst1[0])
m = int(lst2[2]) - int(lst1[2])
s = int(lst2[4]) - int(lst1[4])
if s < 0 :
    s += 60
    m -= 1
if m < 0 :
    m += 60
    h -= 1
if h < 0 :
    h += 24
print(h * 3600 + m * 60 + s)