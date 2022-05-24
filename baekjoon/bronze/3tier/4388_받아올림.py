# https://www.acmicpc.net/problem/4388

while 1 :
    A, B = list(input().split())
    if A == '0' and B == '0' :
        break
    len_a = len(A)
    len_b = len(B)
    if len_a > len_b :
        lst_a = list(A)
        lst_b = ['0'] * (len_a - len_b) + list(B)
    else :
        lst_a = ['0'] * (len_b - len_a) + list(A)
        lst_b = list(B)
    
    answer = 0
    tmp = 0
    for i in range(len(lst_a) - 1, -1, -1) :
        if int(lst_a[i]) + int(lst_b[i]) + tmp > 9 :
            tmp = 1
            answer += 1
        else :
            tmp = 0
    print(answer)