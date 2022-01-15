# https://www.acmicpc.net/problem/1598

a, b = map(int, input().split())
a -= 1
b -= 1
a_col = a // 4
a_row = a % 4
b_col = b // 4
b_row = b % 4
print(abs(a_row - b_row) + abs(a_col - b_col))