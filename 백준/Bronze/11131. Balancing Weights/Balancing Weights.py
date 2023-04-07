for _ in range(int(input())):
    n = int(input())
    _sum = sum([*map(int, input().split())])
    if _sum < 0 : print("Left")
    elif _sum == 0 : print("Equilibrium")
    else : print("Right")
