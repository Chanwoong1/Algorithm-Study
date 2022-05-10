# https://www.acmicpc.net/problem/10867

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst = [str(i) for i in lst]
answer = [lst[0]]
for i in range(1, n) :
    if answer[-1] != lst[i] :
        answer.append(lst[i])
print(' '.join(answer))