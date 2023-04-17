s = [int(i) for i in list(input())]
cnt = 0
lst = []
for i in s:
    if len(lst) == 0:
        lst.append(i)
    elif lst[-1] + 1 == i:
        lst.append(i)
    else:
        if len(lst) == 3:
            cnt += 1
        lst = [i]
if len(lst) == 3:
    cnt += 1
print(cnt)
