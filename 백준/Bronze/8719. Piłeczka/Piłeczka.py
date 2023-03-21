import sys

input = sys.stdin.readline
for _ in range(int(input())) :
    a, b = map(int, input().split())
    cnt = 0
    while a < b :
        a *= 2
        cnt += 1
    print(cnt)
