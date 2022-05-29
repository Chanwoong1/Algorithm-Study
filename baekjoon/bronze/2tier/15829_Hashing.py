# https://www.acmicpc.net/problem/15829

L = int(input())
hash = list(input())
answer = 0
for i in range(L) :
    tmp = abs(96 - ord(hash[i])) * (31 ** i)
    answer += tmp
print(answer % 1234567891)