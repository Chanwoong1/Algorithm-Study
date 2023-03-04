for _ in range(int(input())) :
    st, a, b, c = map(int, input().split())
    if (sum([a, b, c]) < 55 or a < 35 * 0.3 or b < 25 * 0.3 or c < 40 * 0.3) : print(st, sum([a, b, c]), "FAIL")
    else : print(st, sum([a, b, c]), "PASS")
