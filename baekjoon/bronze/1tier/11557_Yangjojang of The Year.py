# https://www.acmicpc.net/problem/11557

from re import S


for _ in range(int(input())) :
    school_lst = []
    alc_lst = []
    N = int(input())
    for _ in range(N) :
        sch, alc = list(input().split())
        school_lst.append(sch)
        alc_lst.append(int(alc))
    for i in range(N) :
        if alc_lst[i] == max(alc_lst) :
            print(school_lst[i])