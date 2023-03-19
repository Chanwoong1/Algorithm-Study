cnt = 2
t1 = int(input())
t2 = int(input())
while True :
    if t1 < t2 : break
    t1, t2 = t2, t1 - t2
    cnt += 1
print(cnt)
