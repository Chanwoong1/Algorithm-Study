from math import factorial
n = int(input())
print((factorial(n - 1) // (factorial(n - 4) * factorial(3))) if n >= 4 else 0)
