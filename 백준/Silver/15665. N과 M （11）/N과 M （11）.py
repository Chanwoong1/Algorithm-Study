from itertools import product

N, M = map(int, input().split())
lst = [*map(int, input().split())]
lst.sort()

lst_set = set()
for i in product(lst, repeat=M):
    if i not in lst_set:
        lst_set.add(i)
        print(*i)
