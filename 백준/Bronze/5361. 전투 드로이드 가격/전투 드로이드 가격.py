droid = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(int(input())) :
    lst = [*map(int, input().split())]
    total = sum([droid[i] * lst[i] for i in range(5)])
    print("${:.2f}".format(total))
