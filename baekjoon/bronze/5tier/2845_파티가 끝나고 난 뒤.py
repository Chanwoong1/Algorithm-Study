# https://www.acmicpc.net/problem/2845

L, P = map(int, input().split())
lst = list(map(int, input().split()))

for i in lst :
    print(i - (L * P), end = ' ')