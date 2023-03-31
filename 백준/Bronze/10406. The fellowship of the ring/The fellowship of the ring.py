ans = 0
W, N, P = map(int, input().split())
for i in [*map(int, input().split())] :
    if i >= W and i <= N : ans += 1
print(ans)
