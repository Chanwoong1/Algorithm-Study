# https://www.acmicpc.net/problem/3058

T = int(input())
for _ in range(T) :
    answer = 100
    sum = 0
    lst = list(map(int, input().split()))
    for i in lst :
        if i % 2 == 0 :
            if answer >= i :
                answer = i
            sum += i
    print(sum, answer)