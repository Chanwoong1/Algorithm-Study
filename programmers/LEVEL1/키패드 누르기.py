'''
https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
'''

def solution(numbers, hand):
    answer = ''
    lastL = 10  # *버튼
    lastR = 12  # #버튼
    
    for n in numbers :
        if n in [1, 4, 7] : # left
            answer += 'L'
            lastL = n
        elif n in [3, 6, 9] :   # right
            answer += 'R'
            lastR = n
        else:
            n = 11 if n == 0 else n 
            
            absL = abs(n-lastL)
            absR = abs(n-lastR)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)): # 오른손의 상하좌우 절댓값이 왼손보다 작을 떄 
                answer+='R' # right
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):   # 반대의 경우
                answer +='L'
                lastL = n
            else:   # 같을 때
                if hand == 'left':  
                    answer+='L'
                    lastL = n
                else:
                    answer+='R'
                    lastR = n
                
    return answer