for _ in range(1, 1 + int(input())) :
    C, B, n, r = [*map(int, input().split())]
    companies = set([*map(int, input().split())])
    r /= 100
    cnt = 0
    for i in range(n) :
        c, p = [*map(int, input().split())]
        if c in companies :
            cnt += int(p * r)
    print(f'Data Set {_}:\n{cnt}\n')
