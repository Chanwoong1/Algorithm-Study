total = 0
n = 2
L = int(input())
R = int(input())
while True :
    if int(L * (R / 100)) <= 5 : break
    total += n * int(L * (R / 100))
    n *= 2
    L = int(L * (R / 100))
print(total)
