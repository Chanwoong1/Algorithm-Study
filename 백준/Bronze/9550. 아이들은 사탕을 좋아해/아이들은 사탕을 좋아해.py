for _ in range(int(input())) :
    N, K = map(int, input().split())
    candy = [*map(int, input().split())]
    answer = sum([i // K for i in candy])
    print(answer)
