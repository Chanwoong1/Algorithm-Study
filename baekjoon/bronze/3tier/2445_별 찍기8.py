# https://www.acmicpc.net/problem/2445

N = int(input())
for i in range(1, N + 1) :
    print('*' * i + ' ' * (N - i) + ' ' * (N - i) + '*' * i)
for i in range(N - 1, -1, -1) :
    print('*' * i + ' ' * (N - i) + ' ' * (N - i) + '*' * i)