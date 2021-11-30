'''
https://programmers.co.kr/learn/courses/30/lessons/12925
'''

def solution(s):
    if s[0] == '-' :        # 맨 앞 문자가 '-'라면
        return -1 * int(s[1:])  # 그것을 제외하고 수치형으로 변환 후 -1 곱해줘서 출력
    else :
        return int(s)       # 아니면 그냥 수치형으로 변환 후 출력