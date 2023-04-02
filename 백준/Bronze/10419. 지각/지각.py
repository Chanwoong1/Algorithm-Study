for _ in range(int(input())) :
    t = int(input())
    for i in range(1, t + 1) :
        if i ** 2 + i > t :
            print(i - 1)
            break
