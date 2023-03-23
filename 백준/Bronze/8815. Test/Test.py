lst = ["ABC", "BCD", "CDA", "DAB"]
for _ in range(int(input())) :
    n = int(input())
    print(lst[((n - 1) // 3) % 4][n % 3 - 1])
