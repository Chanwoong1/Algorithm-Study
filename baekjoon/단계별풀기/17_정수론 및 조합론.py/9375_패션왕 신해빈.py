# https://www.acmicpc.net/problem/9375

from collections import Counter
for _ in range(int(input())) :
    fashion = []
    for _ in range(int(input())) :
        v, k = input().split()
        fashion.append(k)
    num = 1
    result = Counter(fashion)
    for i in result :
        num *= result[i] + 1
    print(num - 1)