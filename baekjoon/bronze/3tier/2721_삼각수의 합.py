# https://www.acmicpc.net/problem/2721

T = int(input())
for _ in range(T) :
    n = int(input())
    T = 0
    sum = 0
    for i in range(1, n + 1) :
        for j in range(1, i + 2) :
            T += j
        sum += i * T
        T = 0
    print(sum)