# https://www.acmicpc.net/problem/2476

N = int(input())
result = []
for _ in range(N) :
    a, b, c = map(int, input().split())
    if a == b and b == c :
        result.append(10000 + 1000 * a)
    elif a == b :
        result.append(1000 + 100 * a)
    elif a == c :
        result.append(1000 + 100 * a)
    elif c == b :
        result.append(1000 + 100 * c)
    else :
        result.append(max(a, b, c) * 100)
print(max(result))