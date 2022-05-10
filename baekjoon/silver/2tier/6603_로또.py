# https://www.acmicpc.net/problem/6603

def lotto(arr, lst, n) :
    if len(arr) == 6 :
        tmp = [str(i) for i in arr]
        print(' '.join(tmp))
    
    else :
        for i in lst :
            if i is not in arr :




while 1 :
    lst = list(map(int, input().split()))
    arr = []
    if lst[0] == 0 :
        break

    n = lst.pop(0)
    lotto(arr, lst, n)    