# https://www.acmicpc.net/problem/9461

T = int(input())
lst = [int(input()) for _ in range(T)]
max_lst = max(lst)
wave = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(7, max_lst) :
    wave.append(wave[i] + wave[i + 1])
for i in lst :
    print(wave[i - 1])