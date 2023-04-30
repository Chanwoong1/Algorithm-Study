ans = 0
for _ in range(int(input())):
    H, B, K = map(int, input().split())
    if H < B:
        ans += (B - H) * K
print(ans)
