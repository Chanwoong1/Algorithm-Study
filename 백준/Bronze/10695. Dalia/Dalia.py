for i in range(1, int(input()) + 1) :
    n, r1, c1, r2, c2 = map(int, input().split())
    if (abs(r2 - r1) == 1 and abs(c2 - c1) == 2) or (abs(r2 - r1) == 2 and abs(c2 - c1) == 1) : print(f"Case {i}: YES")
    else : print(f"Case {i}: NO")
