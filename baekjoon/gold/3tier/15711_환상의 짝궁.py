# https://www.acmicpc.net/problem/15711

import sys
import math

input = sys.stdin.readline

mm=2000001
prime = [0] * mm
prime[1] = 1
for i in range(2, int(math.sqrt(mm)) + 1) :
    if prime[i] == 0 :
        for j in range(i + i, mm, i) :
            prime[j] = 1

q = []
for i in range(2, mm) :
    if prime[i] == 0 :
        q.append(i)

def is_prime(n) : 
    for i in range(0, len(q)) :
        if q[i] * q[i] > n :
            break

        if n % q[i] == 0 :
            return False
    return True

for _ in range(int(input())) :
    A, B = list(map(int, input().split()))
    A += B
    if A < 4 :
        print('NO')
    elif A % 2 == 0 :
        print('YES')
    else :
        A -= 2
        if is_prime(A) == True :
            print('YES')
        else :
            print('NO')