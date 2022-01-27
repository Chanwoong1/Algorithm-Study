# https://www.acmicpc.net/problem/2506

N = int(input())
lst = list(map(int, input().split()))
tmp = 0
tmp_last = 0
answer = 0
for i in lst :
    if i == 1 :
        if tmp_last == 0 :
            answer += i
            tmp += 1
            tmp_last = 1
        else :
            tmp += 1
            answer += tmp
    else :
        tmp_last = 0
        tmp = 0
print(answer)