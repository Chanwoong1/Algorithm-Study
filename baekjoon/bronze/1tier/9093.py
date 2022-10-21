# https://www.acmicpc.net/problem/9093

for i in range(int(input())) :
    s_lst = list(input().split())
    for str in s_lst :
        for j in range(len(str) - 1, -1, -1) :
            print(str[j], end="")
        print(" ", end="")