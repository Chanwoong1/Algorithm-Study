# https://www.acmicpc.net/problem/24087

import math
S = int(input())
A = int(input())
B = int(input())
if S - A > 0 :
    a = math.ceil((S - A) / B)
else :
    a = 0
print(250 + a * 100)