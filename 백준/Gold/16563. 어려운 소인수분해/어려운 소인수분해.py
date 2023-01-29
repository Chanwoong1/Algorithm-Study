N = int(input())
k = list(map(int, input().split()))
prime = [True] * (5000001)
thdlstn = [i for i in range(5000001)]
prime[0] = prime[1] = False
for i in range(5000001) :
    if prime[i] :
        for j in range(2 * i, 5000001, i) :
            prime[j] = False
            if thdlstn[j] == j :
                thdlstn[j] = i

def fn(n) :
    while (n > 1) :
        print(thdlstn[n], end = ' ')
        n //= thdlstn[n]
    if (n != 1) :
        print(int(n), end = ' ')

for kj in k :
    fn(kj)
    print()