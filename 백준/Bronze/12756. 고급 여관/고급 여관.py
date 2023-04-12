A = [*map(int, input().split())]
B = [*map(int, input().split())]
while True :
    B[1] -= A[0]
    A[1] -= B[0]
    if A[1] <= 0 and B[1] <= 0 :
        print("DRAW")
        break
    elif A[1] <= 0 :
        print("PLAYER B")
        break
    elif B[1] <= 0 :
        print("PLAYER A")
        break
