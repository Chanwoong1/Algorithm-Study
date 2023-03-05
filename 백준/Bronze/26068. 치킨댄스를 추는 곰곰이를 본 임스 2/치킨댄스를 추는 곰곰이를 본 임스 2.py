ans = 0
for _ in range(int(input())) :
    s = input()
    if int(s[2:]) <= 90 : ans += 1
print(ans)
