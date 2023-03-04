N = int(input())
S = input()
ans = 0
for i in range(N) :
    if S[i] in ['a', 'e', 'i', 'o', 'u'] : ans += 1
print(ans)
