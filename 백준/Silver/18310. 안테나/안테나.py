N = int(input())
house = [*map(int, input().split())]
house.sort()
mid = house[len(house) // 2 if len(house) % 2 != 0 else len(house) // 2 - 1]
tmp1 = sum([abs(i - mid + 1) for i in house])
tmp2 = sum([abs(i - mid) for i in house])
tmp3 = sum([abs(i - mid - 1) for i in house])
if min(tmp1, tmp2, tmp3) == tmp1:
    print(mid - 1)
elif min(tmp1, tmp2, tmp3) == tmp2:
    print(mid)
else:
    print(mid + 1)
