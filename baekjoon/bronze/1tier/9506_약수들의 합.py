# https://www.acmicpc.net/problem/9506

while 1 :
    n = int(input())
    if n == -1 :
        break
    pf_num = []
    for i in range(n - 1, 0, -1) :
        if n % i == 0 :
            pf_num.append(i)
    if n == sum(pf_num) :
        print(n, "=", end = ' ')
        pf_num.sort()
        pf_num = [str(i) for i in pf_num]
        print(' + '.join(pf_num))
    else :
        print(n, "is NOT perfect.")
