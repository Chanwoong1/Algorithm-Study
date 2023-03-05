n, d = map(int, input().split())
lst = [int(input()) for _ in range(n)]
for i in range(n) : print(int(d * lst[i] / sum(lst)))
