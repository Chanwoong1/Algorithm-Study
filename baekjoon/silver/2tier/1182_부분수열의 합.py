# https://www.acmicpc.net/problem/1182

from itertools import combinations

N, S = list(map(int, input().split()))
lst = list(map(int, input().split()))
answer = 0
for i in range(1, N + 1) :
    for j in combinations(lst, i) :
        if sum(j) == S :
            answer += 1
print(answer)