# https://www.acmicpc.net/problem/1421

N, C, W = map(int, input().split())
tree = [int(input()) for _ in range(N)]
answer = 0
i = max(tree)
for i in range(1, max(tree) + 1) :
    tmp = 0
    for t in tree :
        q, r = divmod(t, i)
        if r :
            cost = q * C
        else :
            cost = (q - 1) * C
        klw = (q * i * W) - cost
        if klw < 0 :
            continue
        tmp += klw
    if answer < tmp :
        answer = tmp
print(answer)