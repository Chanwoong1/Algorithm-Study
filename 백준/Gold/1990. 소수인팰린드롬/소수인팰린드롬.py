a, b = map(int, input().split())
if b > 10000000 :
    b = 10000000
prime = [True] * (10000001)
prime[0] = prime[1] = False
for i in range(10000001) :
    if prime[i] :
        for j in range(2 * i, 10000001, i) :
            prime[j] = False

def _is(n) :
    str_n = str(n)
    if (len(str_n) == 1) :
        return True
    for i in range((len(str_n) // 2)) :
        if (str_n[i] != str_n[len(str_n) - i - 1]) :
            return False
    return True

for i in range(a, b + 1) :
    if prime[i] and _is(i) :
        print(i)
print(-1)