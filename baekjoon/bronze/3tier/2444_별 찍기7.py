# https://www.acmicpc.net/problem/2444

N = int(input())
for i in range(0, N) :
    print(' ' * (N - 1 - i) + '*' * i + '*' + '*' * i)
for i in range(N - 2, -1, -1) :
    print(' ' * (N - 1 - i) + '*' * i + '*' + '*' * i)