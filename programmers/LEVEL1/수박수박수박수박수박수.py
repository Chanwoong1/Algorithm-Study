'''
https://programmers.co.kr/learn/courses/30/lessons/12922
'''

def solution(n):
    s = '수박'
    if n % 2 == 0 :
        return s * (n // 2)
    else :
        answer = s * ((n // 2) + 1)
        return answer[:-1]