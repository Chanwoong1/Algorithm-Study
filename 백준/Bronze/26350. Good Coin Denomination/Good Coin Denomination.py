for _ in range(int(input())) :
    tmp = True
    a, *lst = map(int, input().split())
    print("Denominations:", *lst)
    for i in range(1, len(lst)) :
        if lst[i - 1] * 2 > lst[i] : tmp = False
    if tmp : print("Good coin denominations!")
    else : print("Bad coin denominations!")
    print()
