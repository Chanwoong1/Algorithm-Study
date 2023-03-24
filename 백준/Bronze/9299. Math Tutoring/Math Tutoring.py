for i in range(1, int(input()) + 1) :
    lst = [*map(int, input().split())]
    print("Case {:d}: {:d}".format(i, lst[0] - 1), end = " ")
    cnt = lst[0]
    for j in lst[1 : -1] :
        print(j * cnt, end = " ")
        cnt -= 1
    print()
