for i in range(1, int(input()) + 1) :
    a, b, c, _, d = input().split()
    if b == "+" :
        if int(a) + int(c) == int(d) : print(f"Case {i}: YES")
        else : print(f"Case {i}: NO")
    else :
        if int(a) - int(c) == int(d) : print(f"Case {i}: YES")
        else : print(f"Case {i}: NO")
