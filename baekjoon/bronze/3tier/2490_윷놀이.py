# https://www.acmicpc.net/problem/2490

for _ in range(3) :
    lst = list(map(int, input().split()))
    if sum(lst) == 0 :
        print('D')
    elif sum(lst) == 1 :
        print('C')
    elif sum(lst) == 2 :
        print('B')
    elif sum(lst) == 3 :
        print('A')
    else :
        print('E')