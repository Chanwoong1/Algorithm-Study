import sys

input = sys.stdin.readline
h2s = 3600
m2s = 60
while True:
    M, A, B = map(float, input().split())
    if M == A == B == 0:
        break
    t = round((M / A - M / B) * h2s)
    h = t // h2s
    m = (t % h2s) // m2s
    s = t % m2s
    print("%d:%02d:%02d" % (h, m, s))
