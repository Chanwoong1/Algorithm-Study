'''
https://programmers.co.kr/learn/courses/30/lessons/87389#
'''

def solution(n):
    x = 2
    while n % x != 1 :
        x += 1
    answer = x
    return answer