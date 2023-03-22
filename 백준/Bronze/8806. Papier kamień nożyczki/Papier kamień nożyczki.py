for _ in range(int(input())) :
    X1, Y1, Z1 = map(float, input().split())
    X2, Y2, Z2 = map(float, input().split())
    adam = X1*Y2 + Y1*Z2 + Z1*X2
    gosia = X2*Y1 + Y2*Z1 + Z2*X1
    print("ADAM" if adam > gosia else "GOSIA" if adam < gosia else "=")
