# https://www.acmicpc.net/problem/1421

N, C, W = map(int, input().split())
tree = [int(input()) for _ in range(N)]
answer = 0
i = max(tree)
while i > 0 :
    tmp = []
    for t in tree :
        for _ in range(t // i) :
            tmp.append(i)
        if t % i != 0 :
            tmp.append(t % i)
    cost = (len(tmp) - N) * C
    klw = sum([1 for k in tmp if k == i]) * i * W - cost
    if answer < klw :
        answer = klw
    i -= 1
print(answer)