lst = [i for i in range(21)]
for _ in range(10):
    a, b = map(int, input().split())
    tmp = lst[b : a - 1 : -1]
    for i in range(a, b + 1):
        lst[i] = tmp[i - a]
print(*lst[1:])
