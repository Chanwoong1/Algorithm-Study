while True :
    n = int(input())
    if n == 0 : break
    ans = 0
    for i in range(n) :
        ans += (n - i) ** 2
    print(ans)
