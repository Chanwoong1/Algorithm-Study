cnt = 1
while True :
    lst = list(map(int, input().split()))
    if lst[0] == 0 and len(lst) == 1 : break
    print("Case {:d}: Sorting... done!".format(cnt))
    cnt += 1
