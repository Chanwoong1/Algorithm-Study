for _ in range(int(input())) :
    ans = 0
    for _ in range(int(input())) :
        a, b, c = input().split()
        ans += int(b) * float(c)
    print("${:.2f}".format(ans))
