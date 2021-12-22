# https://www.acmicpc.net/problem/1010

from math import factorial
for _ in range(int(input())) :
    K, N = list(map(int, input().split()))
    result = factorial(N) // (factorial(K) * factorial(N - K))
    print(result)