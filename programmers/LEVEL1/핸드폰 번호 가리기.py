'''
https://programmers.co.kr/learn/courses/30/lessons/12948
'''

def solution(phone_number):
    a = '*' * len(phone_number[ : len(phone_number) - 4])   # 뒤에서 4번째 자리 전까지의 길이만큼 '*' 생성
    b = phone_number[-4 : ]                                 # 뒤에서 4번째 자리부터 끝까지 저장
    return a + b            # 합쳐서 반환