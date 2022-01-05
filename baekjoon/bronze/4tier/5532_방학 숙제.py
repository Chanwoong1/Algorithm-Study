# https://www.acmicpc.net/problem/5532

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
a = (A // C) + (1 if A % C else 0)
b = (B // D) + (1 if B % D else 0)
print(L - max(a, b))