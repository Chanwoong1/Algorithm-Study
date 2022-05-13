# https://www.acmicpc.net/problem/2477

n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
w, w_idx, h, h_idx = 0, 0, 0, 0

for i in range(len(arr)) :
    if arr[i][0] == 1 or arr[i][0] == 2 :
        if w < arr[i][1] :
            w = arr[i][1]
            w_idx = i
    elif arr[i][0] ==3 or arr[i][0] == 4 :
        if h < arr[i][1] :
            h = arr[i][1]
            h_idx = i

sub_w = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
sub_h = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
print(((w * h) - (sub_w * sub_h)) * n)