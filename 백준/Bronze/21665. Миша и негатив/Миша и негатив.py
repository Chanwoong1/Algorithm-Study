n, m = map(int, input().split())
maps = ""
for _ in range(n) : maps += input()
input()
maps2 = ""
for _ in range(n) : maps2 += input()
ans = 0
for i in range(len(maps)) :
    if maps[i] == maps2[i] : ans += 1
print(ans)
