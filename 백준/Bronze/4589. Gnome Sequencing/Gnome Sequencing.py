print("Gnomes:")
for _ in range(int(input())) :
    lst = list(map(int, input().split()))
    result = True
    for i in range(2, len(lst)) :
        result = (lst[i] - lst[i - 1] >= 0 and lst[i - 1] - lst[i - 2] >= 0) or (lst[i] - lst[i - 1] < 0 and lst[i - 1] - lst[i - 2] < 0)
        if result == False :
            break
    if result : print("Ordered")
    else : print("Unordered")
