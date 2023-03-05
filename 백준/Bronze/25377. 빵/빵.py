ans = 1001
for _ in range(int(input())) :
    a, b = map(int, input().split())
    if a <= b :
        if ans > b : ans = b
print(ans)
