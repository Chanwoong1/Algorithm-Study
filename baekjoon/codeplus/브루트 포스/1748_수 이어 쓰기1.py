# https://www.acmicpc.net/problem/1748

N = int(input())
answer = 0
len_n = len(str(N))
i = 1
while i < len_n :
    answer += i * 9 * (10 ** (i - 1))
    i += 1
tmp = N - (10 ** (len_n - 1))
answer += len_n * (tmp + 1)
print(answer)