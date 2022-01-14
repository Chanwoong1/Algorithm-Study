# https://www.acmicpc.net/problem/1267

import math
N = int(input())
lst = list(map(int, input().split()))
y_sum = 0
m_sum = 0
for i in range(N) :
    y_sum += (math.floor(lst[i] / 30) + 1) * 10
    m_sum += (math.floor(lst[i] / 60) + 1) * 15
if y_sum == m_sum :
    print('Y M', y_sum)
elif y_sum < m_sum :
    print('Y', y_sum)
else :
    print('M', m_sum)