for _ in range(int(input())) :
    a, b = map(int, input().split())
    ba = sum([1 for i in str(bin(a))[2:] if i == "1"])
    if (ba % 2 == 0 and b == 0) or (ba % 2 == 1 and b == 1) : print("Valid")
    else : print("Corrupt")
