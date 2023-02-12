def ps(n, r) :
    tmp = r
    cnt = 0
    while n >= tmp :
        cnt += n // tmp
        tmp *= r
    return cnt

def check():
    for num in range(M, 0, -1):
        temp = num
        index = 0
        cnt = 0
        flag = True
        while temp > 1:
            if temp % prime_lst[index] == 0:
                temp //= prime_lst[index]
                cnt += 1
                if cnt > arr[index]:
                    flag = False
                    break
            else:
                cnt = 0
                index += 1
        if flag:
            return num
    return -1

S, F, M = map(int, input().split())
arr = [0] * (M + 1)
prime = [True] * (M + 1)
prime[0] = prime[1] = False
for i in range(int(M ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, M + 1 , i) :
            prime[j] = False
prime_lst = [i for i in range(M + 1) if prime[i]]
for i in range(len(prime_lst)) :
    arr[i] = ps(S + F, prime_lst[i]) - ps(F, prime_lst[i]) - ps(S, prime_lst[i])
print(check())