'''
https://programmers.co.kr/learn/courses/30/lessons/82612
'''

def solution(price, money, count):
    sum = 0
    for i in range(1, count + 1) :
        sum += price * i
    if sum <= money :
        return 0
    else :
        answer = abs(sum - money)
        return answer