'''
https://programmers.co.kr/learn/courses/30/lessons/12932
'''

def solution(n):
    answer = [int(i) for i in str(n)]   # 문자형으로 변환한 n을 한 자씩 수치형으로 변환하면서 리스트 만들어줌
    result = []
    for _ in range(len(answer)) :       # answer의 길이 만큼 반복
        result.append(answer.pop())     # answer의 맨 뒤의 수를 추출 후 result에 추가
    return result