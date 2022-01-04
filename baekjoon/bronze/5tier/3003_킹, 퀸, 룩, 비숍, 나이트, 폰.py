# https://www.acmicpc.net/problem/3003

lst = list(map(int, input().split()))
# king
print(1 - lst[0], end = ' ')
# queen
print(1 - lst[1], end = ' ')
# rook
print(2 - lst[2], end = ' ')
# bishop
print(2 - lst[3], end = ' ')
# knight
print(2 - lst[4], end = ' ')
# pawn
print(8 - lst[5])