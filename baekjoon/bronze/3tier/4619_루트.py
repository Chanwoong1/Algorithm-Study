# https://www.acmicpc.net/problem/4619

while 1 :
    B, N = list(map(int, input().split()))
    if B == 0 and N == 0 :
        break
    
    num = 2
    tmp = 1
    while 1 : 
        num_tmp = 1
        for _ in range(N) :
            num_tmp *= num
        if abs(B - tmp) < abs(B - num_tmp) :
            print(num - 1)
            break
        else :
            tmp = num_tmp
            num += 1
