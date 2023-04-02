n, T = map(int, input().split())
lst = [*map(int, input().split())]
_sum = 0
for i in range(n) :
    _sum += lst[i]
    if _sum > T :
        print(i)
        exit(0)
print(n)
