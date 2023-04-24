s = list(input())
s.sort(reverse=True)
tmp = ""
for i in s:
    tmp += i
if int(tmp) % 10 == 0 and int(tmp) % 3 == 0:
    print(tmp)
else:
    print(-1)
