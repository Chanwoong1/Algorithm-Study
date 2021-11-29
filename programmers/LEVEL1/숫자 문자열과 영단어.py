'''
https://programmers.co.kr/learn/courses/30/lessons/81301
'''

# 딕셔너리
num_dict = {'0' : 'zero', '1' : 'one', '2' : 'two', '3' : 'three', '4' : 'four',
            '5' : 'five', '6' : 'six', '7' : 'seven', '8' : 'eight', '9' : 'nine'}
def solution(s):
    for key, value in num_dict.items() :
        s = s.replace(value, key)   # 영단어를 숫자로 치환
    answer = int(s)
    return answer