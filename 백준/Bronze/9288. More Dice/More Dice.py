for i in range(1, int(input()) + 1) :
    print(f"Case {i}:")
    n = int(input())
    for x in range(1, n // 2 + 1) :
        for y in range(n // 2, 7) :
            if x + y == n : print(f"({x},{y})")
