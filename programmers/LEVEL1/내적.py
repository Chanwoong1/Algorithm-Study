'''
https://programmers.co.kr/learn/courses/30/lessons/70128
'''

def solution(a, b):
    answer = 0
    for i, j in zip(a, b) : # a, b에서 각각 가져오기
        answer += (i * j)   # 곱한 값의 총합
    return answer