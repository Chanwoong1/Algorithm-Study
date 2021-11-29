'''
https://programmers.co.kr/learn/courses/30/lessons/86051
'''

def solution(numbers):
    answer = 45 - sum(numbers)  # 1 ~ 9까지 모두 더한 수는 45, 거기서 받은 숫자들의 합을 빼준다. (중복이 없으므로)
    return answer