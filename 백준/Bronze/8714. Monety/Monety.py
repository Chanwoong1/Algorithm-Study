n = int(input())
m = [*map(int, input().split())]
print(min(n - sum(m), sum(m)))
