for _ in range(int(input())) :
    even, odd = 0, 0
    lst = list(map(int, input().split()))
    for i in lst[1:] :
        if i % 2 == 0 : even += i
        else : odd += i
    if even > odd : print("EVEN")
    elif even < odd : print("ODD")
    else : print("TIE")
