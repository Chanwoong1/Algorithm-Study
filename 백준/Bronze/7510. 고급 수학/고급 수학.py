for i in range(1, int(input()) + 1) :
    print(f"Scenario #{i}:")
    lst = [*map(int, input().split())]
    if (max(lst) ** 2) == (sum(lst) - min(lst) - max(lst)) ** 2 + min(lst) ** 2 : print("yes")
    else : print("no")
    print()
