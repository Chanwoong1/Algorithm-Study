# https://www.acmicpc.net/problem/1270

from collections import Counter

for i in range(int(input())) :
    lst = list(map(int, input().split()))
    N = lst.pop(0)
    c_lst = Counter(lst)
    _max = c_lst.most_common(1)
    if (_max[0][1] > N // 2) :
        print(_max[0][0])
    else :
        print("SYJKGW")