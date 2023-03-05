for _ in range(int(input())) :
    lst = list(map(int, input().split()))
    print(*lst)
    if sum([1 for i in lst if i >= 10]) == 0 : print("zilch")
    elif sum([1 for i in lst if i >= 10]) == 1 : print("double")
    elif sum([1 for i in lst if i >= 10]) == 2 : print("double-double")
    else : print("triple-double")
    print()
