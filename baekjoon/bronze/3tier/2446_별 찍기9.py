# https://www.acmicpc.net/problem/2446

N = int(input())
for i in range(N, 0, -1) :
    print(' ' * (N - i) + '*' * (i - 1) + '*' + '*' * (i - 1))
for i in range(2, N + 1) :
    print(' ' * (N - i) + '*' * (i - 1) + '*' + '*' * (i - 1))