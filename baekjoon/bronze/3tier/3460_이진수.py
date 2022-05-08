# https://www.acmicpc.net/problem/3460

T = int(input())
for _ in range(T) :
    i = 0;
    lst = []
    n = int(input())
    while (n >= 1) :
        if (n % 2 == 1) :
            lst.append(i)
        n = n // 2
        i = i + 1
    print(' '.join(map(str, lst)))
