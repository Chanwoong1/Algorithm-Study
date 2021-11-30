'''
https://programmers.co.kr/learn/courses/30/lessons/12930
'''

def solution(s):
    s = list(s.split(' '))  # 공백 기준 문자열 분리
    result = []
    for i in s :
        ii = list(i)
        for j in range(len(ii)) :
            if j % 2 == 0 :         # 짝수 인덱스는 대문자로
                ii[j] = ii[j].upper()
            else :                  # 홀수 인덱스는 소문자로
                ii[j] = ii[j].lower()
        result.append(''.join(ii))
    answer = ' '.join(result)
    return answer