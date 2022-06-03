# https://www.acmicpc.net/problem/1235

N = int(input())
lst = []
len_ = 100
for _ in range(N) :
    tmp = input()
    if len(tmp) < len_ :
        len_ = len(tmp)
    lst.append(tmp)
for i in range(1, len_ + 1) :
    tmp = []
    for x in lst :
        tmp.append(x[-i :])
    if len(set(tmp)) == N :
        print(i)
        break