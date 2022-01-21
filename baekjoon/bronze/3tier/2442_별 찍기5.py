# https://www.acmicpc.net/problem/2442

N = int(input())
for i in range(0, N) :
    print(' ' * (N - 1 - i) + '*' * i + '*' + '*' * i)