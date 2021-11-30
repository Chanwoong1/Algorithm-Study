'''
https://programmers.co.kr/learn/courses/30/lessons/12931
'''

def solution(n):
    return sum([int(i) for i in str(n)])    # 문자형으로 바꾸어준 n을 한 자씩 수치형으로 변경하면서 리스트로 변환, 그 후 리스트의 총 합 반환