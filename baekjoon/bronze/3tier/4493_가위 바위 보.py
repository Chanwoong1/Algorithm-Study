# https://www.acmicpc.net/problem/4493

t = int(input())
for _ in range(t) :
    p1_win, p2_win = 0, 0
    for _ in range(int(input())) :
        p1, p2 = list(input().split())
        if p1 == p2 :
            continue
        elif (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R') :
            p1_win += 1
        else :
            p2_win += 1
    if p1_win > p2_win :
        print("Player 1")
    elif p1_win < p2_win :
        print("Player 2")
    else :
        print("TIE")