while True :
    D, RH, RV = map(float, input().split())
    if D == RH == RV == 0 : break
    W = 16 * D / (337 ** 0.5)
    H = 9 * W / 16
    print("Horizontal DPI: {:.2f}".format(RH / W))
    print("Vertical DPI: {:.2f}".format(RV / H))
