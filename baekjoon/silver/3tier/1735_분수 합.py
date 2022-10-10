# https://www.acmicpc.net/problem/1735

import math
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
b3 = b1 * b2
a3 = a1 * b2 + a2 * b1
gcd = math.gcd(a3, b3)
print(a3 // gcd, b3 // gcd)