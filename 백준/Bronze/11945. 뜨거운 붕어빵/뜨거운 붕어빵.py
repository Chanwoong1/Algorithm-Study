N, M = map(int, input().split())
for _ in range(N) :
    s = input()
    for i in range(M - 1, -1, -1) : print(s[i], end = "")
    print()
