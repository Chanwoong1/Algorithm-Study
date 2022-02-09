# https://www.acmicpc.net/problem/2953

result = []
for _ in range(5) :
    result.append(sum(list(map(int, input().split()))))
print(result.index(max(result)) + 1, max(result))