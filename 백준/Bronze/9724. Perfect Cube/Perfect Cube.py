for i in range(1, int(input()) + 1) :
    A, B = map(int, input().split())
    cnt = 0
    x = 1
    while x ** 3 <= B :
        if x ** 3 >= A : cnt += 1
        x += 1
    print(f"Case #{i}: {cnt}")
