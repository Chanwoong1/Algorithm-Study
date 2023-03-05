a, b = map(int, input().split())
for _ in range(int(input())) :
    n = int(input())
    if n <= 1000 : print(n, n * a)
    else : print(n, 1000 * a + (n - 1000) * b)
