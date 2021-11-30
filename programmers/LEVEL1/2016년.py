'''
https://programmers.co.kr/learn/courses/30/lessons/12901#
'''

def solution(a, b):
    cal = {1 : 31, 2 : 29, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    n = 0
    for i in range(1, a) :
        n += cal[i]
    n += b
    days = days * ((n // 7) + 1)
    answer = days[n - 1]
    return answer