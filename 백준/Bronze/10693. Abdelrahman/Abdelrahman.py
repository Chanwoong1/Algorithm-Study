for i in range(1, int(input()) + 1) :
    N, M = map(int, input().split())
    print(f"Case {i}:", M - (N - 1))
