# https://www.acmicpc.net/problem/1676

from math import factorial
N = list(str(factorial(int(input()))))
n = 0
while 1 :
    if N.pop() != '0' :
        break
    n += 1
print(n)