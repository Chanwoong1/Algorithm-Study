# https://www.acmicpc.net/problem/2547

T = int(input())
for _ in range(T) :
    lst = []
    input()
    N = int(input())
    for _ in range(N) :
        lst.append(int(input()))

    if sum(lst) % N == 0 :
        print('YES')
    else :
        print('NO')