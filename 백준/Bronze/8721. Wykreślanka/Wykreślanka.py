n = int(input())
lst = [*map(int, input().split())]
cnt = 0
idx = 1
for i in range(n) :
    if lst[i] != idx : cnt += 1
    else : idx += 1
print(cnt)
