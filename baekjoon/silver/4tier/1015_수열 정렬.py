# https://www.acmicpc.net/problem/1015

N = int(input())
lst = list(map(int, input().split()))
lst_sort = sorted(lst)
answer = []
for i in range(N) :
    idx = lst_sort.index(lst[i])
    answer.append(idx)
    lst_sort[idx] = -1
print(*answer)