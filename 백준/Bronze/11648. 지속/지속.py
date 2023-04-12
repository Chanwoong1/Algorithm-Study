n = int(input())
cnt = 0
while n > 9 :
    tmp = 1
    for i in list(str(n)) :
        tmp *= int(i)
    n = tmp
    cnt += 1
print(cnt)
