# https://www.acmicpc.net/problem/2981


''' 시간초과
N = int(input())
lst = sorted([int(input()) for _ in range(N)])
result = []
M = lst.pop(0)
i = 2
while i <= lst[-1] :
    tmp = M % i
    result.append(i)
    for j in lst :
        if j % i != tmp :
            result.remove(i)
            break
    i += 1
result = [str(i) for i in result]
print(' '.join(result))
'''

def getGCD(a, b) :
    r = a % b
    while r != 0 :
        a = b
        b = r
        r = a % b
    return b

N = int(input())
lst = sorted([int(input()) for _ in range(N)])

gcd = lst[1] - lst[0]
for i in range(2, N) :
    gcd = getGCD(gcd, lst[i] - lst[i - 1])

result = [gcd]
for i in range(2, int(gcd ** 0.5) + 1) :
    if gcd % i == 0 :
        print(i, end = ' ')
        if i != gcd // i :
            result.insert(0, gcd // i)
        
for num in result :
    print(num, end = ' ')