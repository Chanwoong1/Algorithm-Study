from math import factorial
N, K = map(int, input().split())
p = 10 ** 9 + 7
print(factorial(N) * pow((factorial(N - K) * factorial(K)), -1, p) % p)