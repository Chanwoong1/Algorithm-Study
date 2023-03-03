for _ in range(int(input())) :
    h, w = map(int, input().split())
    for _ in range(w) :
        for _ in range(h) :
            print("X", end = "")
        print()
    print()
