# https://www.acmicpc.net/problem/16199

date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))

# 1
y1 = date2[0] - date1[0]
m1 = date2[1] - date1[1]
d1 = date2[2] - date1[2]
if d1 < 0 :
    m1 -= 1
if m1 < 0 :
    y1 -= 1
print(y1)

# 2
y2 = date2[0] - date1[0]
print(y2 + 1)

# 3
y3 = date2[0] - date1[0]
print(y3)