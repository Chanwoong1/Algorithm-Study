# https://www.acmicpc.net/problem/11051

from math import factorial
N, K = list(map(int, input().split()))
result = factorial(N) // (factorial(K) * factorial(N - K))
print(result % 10007)