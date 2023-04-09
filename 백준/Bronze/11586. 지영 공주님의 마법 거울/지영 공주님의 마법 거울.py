lst = []
for _ in range(int(input())) :
    lst.append(input())
K = int(input())
if K == 1 :
    for i in lst : print(i)
elif K == 2 :
    for i in lst : print(i[-1::-1])
else :
    for i in range(len(lst) - 1, -1, -1) : print(lst[i])
