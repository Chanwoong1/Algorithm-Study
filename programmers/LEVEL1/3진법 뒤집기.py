'''
https://programmers.co.kr/learn/courses/30/lessons/68935
'''

def solution(n):
    three = ''
    while n >= 3 :  # 3진법으로 변환 후 앞뒤 반전까지
        three += str(n % 3)
        n = (n // 3)
    three += str(n % 3)
    
    ten = 0
    for i in range(len(three) - 1, -1, -1) :    # 문자열 끝에서부터 10진법 표현 계산 시작
        if i == len(three) - 1 :
            ten += int(three[i])
        else :
            m = len(three) - 1 - i
            ten += int(three[i]) * (3 ** m)
               
    return ten