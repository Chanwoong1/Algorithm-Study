for _ in range(int(input())) :
    a, b = input().split()
    bw_a, bw_b = "", ""
    for i in range(len(a) - 1, -1, -1) : bw_a += a[i]
    for i in range(len(b) - 1, -1, -1) : bw_b += b[i]
    bw_sum = int(bw_a) + int(bw_b)
    ans = ""
    for i in range(len(str(bw_sum)) - 1, -1, -1) : ans += str(bw_sum)[i]
    print(int(ans))
