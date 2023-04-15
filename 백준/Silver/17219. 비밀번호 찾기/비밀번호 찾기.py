N, M = map(int, input().split())
pw = dict()
for _ in range(N) :
    a, b = input().split()
    pw[a] = b
for _ in range(M) :
    print(pw[input()])
