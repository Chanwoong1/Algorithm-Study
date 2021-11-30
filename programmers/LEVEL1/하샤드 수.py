'''
https://programmers.co.kr/learn/courses/30/lessons/12947
'''

def solution(x):
    h = sum([int(i) for i in str(x)])   # 자릿수의 합
    if x % h == 0 :                     # 하샤드의 수 조건
        return True
    else :
        return False