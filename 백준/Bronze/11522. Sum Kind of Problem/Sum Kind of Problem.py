for _ in range(int(input())):
    k, n = map(int, input().split())
    print(k, end=" ")
    print(n * (n + 1) // 2, end=" ")
    print(int((2 * n) * (2 * n + 1) / 4 - n / 2), end=" ")
    print(int((2 * n) * (2 * n + 1) / 4 + n / 2))
