'''
https://programmers.co.kr/learn/courses/30/lessons/12933
'''

def solution(n):
    answer = int(''.join(sorted([i for i in str(n)], reverse = True))) # 문자형으로 변환한 n을 리스트로 변환하여 역순으로 정렬 후 수치형으로 반환
    return answer