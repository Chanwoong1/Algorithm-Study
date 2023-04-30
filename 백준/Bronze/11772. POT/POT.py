ans = 0
for _ in range(int(input())):
    s = input()
    n, pot = int(s[:-1]), int(s[-1])
    ans += n**pot
print(ans)
