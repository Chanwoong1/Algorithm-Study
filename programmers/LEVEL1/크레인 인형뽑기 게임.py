'''
https://programmers.co.kr/learn/courses/30/lessons/64061
'''

def solution(board, moves):
    result = 0
    lastn = []
    for i in moves :
        n = 0   # 초기화
        for j in range(len(board)) :    # 위에서부터 탐색
            if n == 0 : # n = 0일때 코드 돌아감
                if board[j][i - 1] != 0 :   # 인형이 걸릴 때
                    n = board[j][i - 1]
                    if len(lastn) == 0 :    # 첫 인형이라면
                        lastn.append(n)     # 인형 바구니에 추가
                        board[j][i - 1] = 0 # 첫 인형 뽑고 0으로 바꾸기
                    else :                  # 그 다음부터
                        lp = lastn.pop()    # 바구니와 비교위해
                        if lp == n :        # 방금 뽑은 n인형과 바구니에서 가장 최근에 뽑힌 lp 인형과 비교
                            result += 1     # 맞았을 때 
                            board[j][i - 1] = 0 # 그리고 0으로 바꾸기
                            break
                        else :      # 비교 아닐떄
                            lastn.append(lp)    # 바구니에 다시 넣어주기
                            lastn.append(n)     # 바구니에 새로 추가
                            board[j][i - 1] = 0 # 0으로 변경
            else :
                pass      
            
    answer = result * 2 # 터뜨린 횟수마다 인형은 두개씩 없어진다
    return answer