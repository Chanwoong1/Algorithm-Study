# https://www.acmicpc.net/problem/1331

visit = [[0] * 6 for _ in range(6)]
answer = 0
for ii in range(36) :
    tmp = input()
    i = abs(65 - ord(tmp[0]))
    j = int(tmp[1]) - 1
    if ii == 0 :
        start_i = i
        start_j = j
    if ii != 0 :
        if (abs(last_i - i) == 2 and abs(last_j - j) == 1) or (abs(last_i - i) == 1 and abs(last_j - j) == 2) :
            pass
        else :
            answer = 1
    if visit[i][j] == 0 :
        visit[i][j] = 1
    else :
        answer = 1
    last_i = i
    last_j = j
if answer == 0 :
    if (abs(start_i - i) == 2 and abs(start_j - j) == 1) or (abs(start_i - i) == 1 and abs(start_j - j) == 2) :
        print('Valid')
    else :
        print('Invalid')
else :
    print('Invalid')