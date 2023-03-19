for i in range(1, int(input()) + 1) :
    print(f"Scenario #{i}:")
    n, m = map(int, input().split())
    nn = (n - 1) * n // 2
    mm = (m + 1) * m // 2
    print(mm - nn)
    print()
