'''
https://programmers.co.kr/learn/courses/30/lessons/12917
'''

def solution(s):
    s = sorted(list(s), reverse = True) # 리스트로 하나씩 쪼개어 내림차순 정렬
    return ''.join(s)