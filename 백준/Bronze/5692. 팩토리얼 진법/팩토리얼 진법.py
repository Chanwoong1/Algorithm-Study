from math import factorial
import sys

input = sys.stdin.readline
while True :
    n = int(input())
    if n == 0 : break
    n = str(n)
    ln = len(n)
    ans = 0
    for i in range(ln) :
        ans += int(n[i]) * factorial(ln - i)
    print(ans)
