for _ in range(int(input())) :
    ans = 0
    s = input()
    while ans < len(s) and s[ans] == "U" : ans += 1
    print(ans)
