a, b = 0, 0
for _ in range(int(input())) :
    aa, bb = map(int, input().split())
    if aa > bb : a += aa + bb
    elif aa < bb : b += aa + bb
    else :
        a += aa
        b += bb
print(a, b)
