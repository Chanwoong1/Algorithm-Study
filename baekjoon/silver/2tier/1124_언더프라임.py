# https://www.acmicpc.net/problem/1124

import math

def is_prime(n) :
    if 2 > n :
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
lst = []
A, B = map(int, input().split())
for i in range(A, B + 1) :
    n = 2
    i_lst = []
    while i >= n :
        while i % n == 0 :
            if (is_prime(n)) :
                i_lst.append(n)
            i /= n
        n += 1
    if (len(i_lst) > 0) :
	    lst.append(i_lst)
answer = 0
for i in lst :
    if (is_prime(len(i))) :
        answer += 1
print(answer)