# https://www.acmicpc.net/problem/1064

xa, ya, xb, yb, xc, yc = map(int, input().split())
if ((xa - xb) * (ya - yc) == (ya - yb) * (xa - xc)) :
    print(-1.0)
    exit()

ab = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
ac = ((xa - xc) ** 2 + (ya - yc) ** 2) ** 0.5
bc = ((xc - xb) ** 2 + (yc - yb) ** 2) ** 0.5
lst = [ab, ac, bc]
print(2 * (max(lst) - min(lst)))