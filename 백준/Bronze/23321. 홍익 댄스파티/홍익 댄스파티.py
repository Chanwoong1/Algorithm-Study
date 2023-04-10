lst = list(input())
for _ in range(4) :
    tmp = list(input())
    for i in range(len(tmp)) :
        lst[i] += tmp[i]
for i in range(len(lst)) :
    if lst[i] == ".omln" : lst[i] = "owln."
    elif lst[i] == "owln." : lst[i] = ".omln"
for i in range(5) :
    for j in range(len(lst)) :
        print(lst[j][i], end = "")
    print()
