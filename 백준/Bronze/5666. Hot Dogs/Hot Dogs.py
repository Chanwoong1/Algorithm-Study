try :
    while True :
        a, b = map(int, input().split())
        print("{:.2f}".format(a / b))
except :
    exit(0)
