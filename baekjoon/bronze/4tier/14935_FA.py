# https://www.acmicpc.net/problem/14935

x = input()
def f(x) :
    return x[0] * len(x)
n = 10000
while n > 0 :
    tmp = f(x)
    if x == tmp :
        print('FA')
        break
    
    x = tmp
    n -= 1
if n == 0 :
    print('NFA')