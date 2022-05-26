# https://www.acmicpc.net/problem/1063

king, stone, N = list(input().split())
lst = [input() for _ in range(int(N))]
king_x = abs(65 - ord(king[0]))
king_y = int(king[1]) - 1
stone_x = abs(65 - ord(stone[0]))
stone_y = int(stone[1]) - 1
for com in lst :
    if com == 'R' :
        if king_y == stone_y and king_x + 1 == stone_x :
            if stone_x != 7 :
                stone_x += 1
                king_x += 1
        else :
            if king_x != 7 :
                king_x += 1
    elif com == 'L' :
        if king_y == stone_y and king_x - 1 == stone_x :
            if stone_x != 0 :
                stone_x -= 1
                king_x -= 1
        else :
            if king_x != 0 :
                king_x -= 1
    elif com == 'B' :
        if king_x == stone_x and king_y - 1 == stone_y :
            if stone_y != 0 :
                stone_y -= 1
                king_y -= 1
        else :
            if king_y != 0 :
                king_y -= 1
    elif com == 'T' :
        if king_x == stone_x and king_y + 1 == stone_y :
            if stone_y != 7 :
                stone_y += 1
                king_y += 1
        else :
            if king_y != 7 :
                king_y += 1
    elif com == 'RT' :
        if king_y + 1 == stone_y and king_x + 1 == stone_x :
            if stone_x != 7 and stone_y != 7 :
                stone_x += 1
                stone_y += 1
                king_x += 1
                king_y += 1
        else :
            if king_x != 7 and king_y != 7 :
                king_x += 1
                king_y += 1
    elif com == 'LT' :
        if king_x - 1 == stone_x and king_y + 1 == stone_y :
            if stone_x != 0 and stone_y != 7 :
                stone_x -= 1
                stone_y += 1
                king_x -= 1
                king_y += 1
        else :
            if king_x != 0 and king_y != 7 :
                king_x -= 1
                king_y += 1
    elif com == 'RB' :
        if king_y - 1 == stone_y and king_x + 1 == stone_x :
            if stone_x != 7 and stone_y != 0 :
                stone_x += 1
                stone_y -= 1
                king_x += 1
                king_y -= 1
        else :
            if king_x != 7 and king_y != 0 :
                king_x += 1
                king_y -= 1
    else :
        if king_y - 1 == stone_y and king_x - 1 == stone_x :
            if stone_x != 0 and stone_y != 0 :
                stone_x -= 1
                stone_y -= 1
                king_x -= 1
                king_y -= 1
        else :
            if king_x != 0 and king_y != 0 :
                king_x -= 1
                king_y -= 1
x_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print(x_lst[king_x] + str(king_y + 1))
print(x_lst[stone_x] + str(stone_y + 1))