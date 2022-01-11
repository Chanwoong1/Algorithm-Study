# https://www.acmicpc.net/problem/15025

lst = list(map(int, input().split()))
if sum(lst) == 0 :
    print('Not a moose')
elif sum(lst) == max(lst) * 2 :
    print('Even', sum(lst))
else :
    print('Odd', max(lst) * 2)