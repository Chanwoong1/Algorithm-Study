n = int(input())
m = sum([*map(int, input().split())])
print(min(n - m, m))
