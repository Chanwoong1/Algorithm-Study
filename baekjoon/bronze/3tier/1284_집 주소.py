# https://www.acmicpc.net/problem/1284

while 1 :
    num = int(input())
    if num == 0 :
        break

    num = list(str(num))
    res = 0
    for i in num :
        if i == '1' :
            res += 2
        elif i == '0' :
            res += 4
        else :
            res += 3
    
    res += len(num) + 1

    print(res)