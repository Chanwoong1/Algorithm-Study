# https://www.acmicpc.net/problem/7567

lst = input()
answer = 10
for i in range(1, len(lst)) :
    if lst[i] == lst[i - 1] :
        answer += 5
    else :
        answer += 10
print(answer)