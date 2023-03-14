for i in range(1, int(input()) + 1) :
    b, w = map(float, input().split())
    ans = 0
    for _ in range(int(b)) :
        ans += (float(input()) ** 3) * 4 / 3 * 3.14159265358979323 / 1000
    print(f'Data Set {i}:')
    if ans >= w : print("Yes")
    else : print("No")
    print()
