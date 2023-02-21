n, k = map(int, input().split())
sig = [list(map(int, input().split())) for _ in range(k)]
sig.sort(key = lambda x : x[0])
time, dist = 0, 0
for x, t, s in sig :
    time += x - dist
    tmp = (time - s) // t
    if tmp % 2 == 1 :
        time = (tmp + 1) * t + s
    dist = x
time += n - dist
print(time)