# https://www.acmicpc.net/problem/1259

while 1 :
    lst = list(input())
    if len(lst) == 1 and lst[0] == '0' :
        break
    yes = 0
    for i in range(len(lst) // 2) :
        if lst[i] != lst[len(lst) - 1 - i] :
            yes = 1
    if yes == 0 :
        print('yes')
    else :
        print('no')