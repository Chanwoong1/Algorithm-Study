for _ in range(int(input())):
    lst = [0] * 26
    a, b = input().split()
    for i in list(a):
        lst[ord(i) - 97] += 1
    for i in list(b):
        lst[ord(i) - 97] -= 1
    if min(lst) == max(lst) == 0:
        print("Possible")
    else:
        print("Impossible")
