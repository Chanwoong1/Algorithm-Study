n = int(input())
l, r, ans= 0, 0, 0
while l <= 5 and r <= 5 :
    if l + r == n and l >= r :
        ans += 1
        r += 1
        l = 0
    if l == 5 : r += 1
    else : l += 1
print(ans)
