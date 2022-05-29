# https://www.acmicpc.net/problem/2920

lst = list(map(int, input().split()))
asc = 0
des = 0
for i in range(len(lst) - 1) :
    if lst[i] > lst[i + 1] :
        des += 1
    elif lst[i] < lst[i + 1] :
        asc += 1
if asc == len(lst) - 1 :
    print('ascending')
elif des == len(lst) - 1 :
    print('descending')
else :
    print('mixed')