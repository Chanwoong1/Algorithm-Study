# https://www.acmicpc.net/problem/10039

tmp = 0
for _ in range(5) :
    i = int(input())
    if i < 40 :
        tmp += 40
    else :
        tmp += i
print(tmp // 5)