# https://www.acmicpc.net/problem/5717

while 1 :
    M, F = list(map(int, input().split()))
    if M == 0 & F == 0 :
        break
    print(M + F)