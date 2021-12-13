# https://www.acmicpc.net/problem/1003

N = int(input())
lst = [int(input()) for _ in range(N)]
lst_max = max(lst)
zero = [1, 0, 1]
one = [0, 1, 1]


for j in range(3, lst_max + 1) :
    zero.append(zero[j-1] + zero[j-2])
    one.append(one[j-1] + one[j-2])

for i in lst :
    print(zero[i], one[i])