for _ in range(int(input())):
    N, C = map(int, input().split())
    print(N // C + (1 if N % C != 0 else 0))
