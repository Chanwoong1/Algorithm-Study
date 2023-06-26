lst = [0, 9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000]
N, K = map(int, input().split())
num = 0
for i in range(1, len(lst)):
    if lst[i] < N:
        num += lst[i] * i
        N -= lst[i]
    else:
        num += N * i
        break

if num < K:
    print(-1)
else:
    for i in range(1, len(lst)):
        if lst[i] * i < K:
            K -= lst[i] * i
        else:
            print(str(10 ** (i - 1) + (K - 1) // i)[(K - 1) % i])
            break
