# https://www.acmicpc.net/problem/1358

def calc_dist(x, y, a, b) :
    return ((x - a) * (x - a)) + ((b - y) * (b - y))

cnt = 0
W, H, X, Y, P = map(int, input().split())

for t in range(P) :
    x, y = map(int, input().split())
    r = (H / 2) ** 2
    if (X <= x and x <= X + W and Y <= y and y <= Y + H):
        cnt += 1
    elif (calc_dist(X, Y + (H / 2), x, y) <= r):
        cnt += 1
    elif (calc_dist(X + W, Y + (H / 2), x, y) <= r):
        cnt += 1
print(cnt)