try:
    while True :
        A, B, C = map(int, input().split())
        print(max(C - B, B - A) - 1)
except:
    exit(0)
