# https://www.acmicpc.net/problem/10817

lst = list(map(int, input().split()))
print(sum(lst) - min(lst) - max(lst))