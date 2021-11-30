'''
https://programmers.co.kr/learn/courses/30/lessons/12943
'''

def solution(num):
    n = 0
    while num != 1 :
        if num % 2 == 0 :   # 짝수라면
            num = num // 2
            n += 1
        else :              # 홀수라면
            num = num * 3 + 1
            n += 1
        
        if n == 500 :       # 500번 반복해도 1이 안된다면 
            return -1       # -1 반환
    return n