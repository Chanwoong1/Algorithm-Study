N = int(input())
lst = list(map(int, input().split()))
prime = [True] * 1000001
thdlstn = [i for i in range(1000001)]
prime[0] = prime[1] = False
for i in range(1001) :
    if prime[i] :
        for j in range(2 * i, 1000001, i) :
            prime[j] = False
            if thdlstn[j] == j :
                thdlstn[j] = i

prime_lst = [i for i in range(1000001) if prime[i]]
whole = [0] * 1000001

def fn(n) :
    ret = [0] * len(prime_lst)
    while (n > 1) :
        ret[prime_lst.index(thdlstn[n])] += 1
        whole[thdlstn[n]] += 1
        n //= thdlstn[n]
    if (n != 1) :
        whole[thdlstn[n]] += 1
        ret[prime_lst.index(thdlstn[n])] += 1
    return ret


ans = []
for i in lst :
    ans.append(fn(i))
# print(prime_lst[ : 10])
# print(thdlstn[ : 10])
# print(whole[ : 10])
# for i in ans :
#     print(i[ : 10])
answer = 1
count = 0
for i in range(len(prime_lst)) :
    cnt = whole[prime_lst[i]] // N
    # print(cnt, end = ' ')
    for j in range(N) :
        if cnt > ans[j][i] :
            # print('here', end = ' ')
            count += cnt - ans[j][i]
    answer *= prime_lst[i] ** cnt
print(answer, count)