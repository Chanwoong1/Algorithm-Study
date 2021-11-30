'''
https://programmers.co.kr/learn/courses/30/lessons/12919
'''

def solution(seoul):
    n = 0       # 0번째 인덱스부터 시작
    while 1 :
        if seoul[n] == 'Kim' :
            return '김서방은 {}에 있다'.format(n)
        n += 1