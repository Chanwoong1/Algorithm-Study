# https://www.acmicpc.net/problem/2443

N = int(input())
for i in range(N - 1, -1, -1) :
    print(' ' * (N - 1 - i) + '*' * i + '*' + '*' * i)