cnt = 1
while True :
    N = int(input())
    if N < 0 : break
    sum_x, sum_y, sum_m = 0, 0, 0
    for _ in range(N) :
        x, y, m = map(float, input().split())
        sum_x += x * m
        sum_y += y * m
        sum_m += m
    print("Case {:d}: {:.2f} {:.2f}".format(cnt, sum_x / sum_m, sum_y / sum_m))
    cnt += 1
    input()

