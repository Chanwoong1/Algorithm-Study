# https://www.acmicpc.net/problem/20233

a = int(input())
x = int(input()) * 21
b = int(input())
y = int(input()) * 21
T = int(input())
if T <= 30 :
    print(a, b)
elif T <= 45 :
    print(a + (T - 30) * x, b)
else :
    print(a + (T - 30) * x, b + (T - 45) * y)