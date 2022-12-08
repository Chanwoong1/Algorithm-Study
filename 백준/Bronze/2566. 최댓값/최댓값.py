lst = []
max_lst = []
for i in range(9) :
    tmp = list(map(int, input().split()))
    max_lst.append(max(tmp))
    lst.append(tmp)
print(max(max_lst))
print(max_lst.index(max(max_lst)) + 1, lst[max_lst.index(max(max_lst))].index(max(max_lst)) + 1)