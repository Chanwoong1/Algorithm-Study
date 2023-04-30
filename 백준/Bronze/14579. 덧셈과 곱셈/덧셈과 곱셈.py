a, b = map(int, input().split())
ans = 1
for i in range(a, b + 1):
    ans *= sum([i for i in range(1, i + 1)])
print(ans % 14579)
