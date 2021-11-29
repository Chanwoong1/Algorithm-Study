'''
https://programmers.co.kr/learn/courses/30/lessons/76501
'''

def solution(absolutes, signs):
    answer = 0
    for i, j in zip(absolutes, signs) : # 각각 가져오기
        if j == 1 : # sign == True
            answer += abs(i)    # plus
        else :
            answer -= abs(i)    # minus
    return answer