for _ in range(int(input())):
    n = int(input())
    lst = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            lst[j] = 1 if lst[j] == 0 else 0
    print(sum(lst))
