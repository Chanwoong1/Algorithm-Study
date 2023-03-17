case = 1
while True :
    s = int(input())
    if s == 0 : break
    s = s / 2 + int(s % 2)
    s += s / 2
    print(f"File #{case}")
    print("John needs {:d} floppies.".format(int((s + 62 * 30000 - 1) / (62 * 30000))))
    print()
    case += 1
