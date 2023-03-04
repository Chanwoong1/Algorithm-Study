for _ in range(int(input())) :
    a, b = map(int, input().split())
    if a > b : a, b = b, a
    a_lst = []
    b_lst = []
    while a > 0 :
        a_lst.append(a)
        a //= 2
    while b > 0 :
        b_lst.append(b)
        b //= 2
    a_lst.sort()
    b_lst.sort()
    ans = 1
    for i in range(len(a_lst)) :
        if a_lst[i] == b_lst[i] : ans = a_lst[i]
    print(ans * 10)
