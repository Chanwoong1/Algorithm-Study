lst = list(map(int, input().split()))
A, B = min(lst), max(lst)
if B - A > 1:
    print(B - A - 1)
    print(*[i for i in range(A + 1, B)])
else:
    print(0)
