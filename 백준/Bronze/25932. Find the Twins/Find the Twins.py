for _ in range(int(input())) :
    lst = list(map(int, input().split()))
    print(*lst)
    if 17 in lst and 18 in lst : print("both")
    elif 17 in lst : print("zack")
    elif 18 in lst : print("mack")
    else : print("none")
    print()
