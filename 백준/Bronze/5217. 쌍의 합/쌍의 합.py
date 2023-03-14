for _ in range(int(input())) :
    n = int(input())
    print(f"Pairs for {n}:", end = " ")
    if n > 2 :
        for i in range(1, n // 2 + 1) :
            if i == n // 2 and i != n - i : print(i, n - i, end ="")
            elif i != n - i :
                if i + 1 == n // 2 and i + 1 == n - i - 1 : print(i, n - i, end = "")
                else : print(i, n - i, end = ", ")
    print()
