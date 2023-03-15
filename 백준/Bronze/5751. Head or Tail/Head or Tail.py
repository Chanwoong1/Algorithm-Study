while True :
    n = int(input())
    if n == 0 : break
    j = sum([*map(int, input().split())])
    print("Mary won {:d} times and John won {:d} times".format(n - j, j))
