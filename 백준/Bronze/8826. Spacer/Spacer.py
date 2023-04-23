for i in range(int(input())):
    int(input())
    x, y = 0, 0
    c = input()
    for i in list(c):
        if i == "E":
            x += 1
        elif i == "W":
            x -= 1
        elif i == "N":
            y += 1
        elif i == "S":
            y -= 1
    print(abs(x) + abs(y))
