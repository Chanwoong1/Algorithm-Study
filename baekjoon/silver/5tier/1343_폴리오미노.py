# https://www.acmicpc.net/problem/1343

board = list(input())
len_board = len(board)
idx = 0
answer = []
while idx < len_board :
    if board[idx] == 'X' :
        x_num = 0
        j = 0
        while idx + j < len_board :
            if board[idx + j] == 'X' :
                x_num += 1
                j += 1
            else :
                break
        if x_num % 2 == 0 :
            for i in range(x_num // 4) :
                answer.append('AAAA')
            for i in range((x_num % 4) // 2) :
                answer.append('BB')
        else :
            print(-1)
            exit()
        idx += j
    else :
        answer.append('.')
        idx += 1

print(''.join(answer))