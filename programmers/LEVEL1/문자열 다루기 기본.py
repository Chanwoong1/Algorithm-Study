'''
https://programmers.co.kr/learn/courses/30/lessons/12918
'''

def solution(s):
    if len(s) > 8 or len(s) < 1 :       # 문자열 s의 길이는 1 이상 8 이하
        return False
    elif len(s) == 4 or len(s) == 6 :   # 문자열 s의 길이는 4 이거나 6
        s = list(s)
        try : 
            [int(i) for i in s]         # 숫자로만 구성되어 있다면 이게 돌아간다
            return True
        except :                        # 안되면 False를 반환
            return False
    else :
        return False