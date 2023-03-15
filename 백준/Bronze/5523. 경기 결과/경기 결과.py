a, b = 0, 0
for i in range(int(input())) :
    aa, bb = map(int, input().split())
    if aa > bb : a += 1
    elif aa < bb : b += 1
print(a, b)
