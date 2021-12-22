# https://www.acmicpc.net/problem/2609

N, M = sorted(list(map(int, input().split())))

# 최대공약수
max_ = N
while 1 :
    if N % max_ == 0 and M % max_ == 0 :
        print(max_)
        break
    max_ -= 1

# 최소공배수
i = 1
while 1 :
    if (N * i) % M == 0 :
        print(N * i)
        break
    i += 1