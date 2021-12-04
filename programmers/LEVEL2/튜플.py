'''
https://programmers.co.kr/learn/courses/30/lessons/64065
'''

from collections import Counter
def solution(s):
    ss = s.split('},{')
    ss = [i.replace('{{', '') for i in ss]
    ss = [i.replace('}}', '') for i in ss]
    ss = [i.split(',') for i in ss]
    ss = [element for array in ss for element in array]

    counter = Counter(ss).most_common()
    result = []
    for key in counter :
        result.append(int(key[0]))
    return result