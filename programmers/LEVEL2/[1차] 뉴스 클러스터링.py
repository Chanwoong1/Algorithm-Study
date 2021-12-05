'''
https://programmers.co.kr/learn/courses/30/lessons/17677
'''

import math
def solution(str1, str2):
    answer1 = 0
    answer2 = 0
    str1 = str1.lower()
    str2 = str2.lower()
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    str1_lst = [str1[i] + str1[i+1] for i in range(len(str1) - 1) if str1[i] in alpha and str1[i + 1] in alpha]
    str2_lst = [str2[i] + str2[i+1] for i in range(len(str2) - 1) if str2[i] in alpha and str2[i + 1] in alpha]
    # 교집합
    for i in str1_lst :
        if i in str2_lst :
            answer1 += 1
            str2_lst.remove(i)
    # 합집합
    str2_lst = [str2[i] + str2[i+1] for i in range(len(str2) - 1) if str2[i] in alpha and str2[i + 1] in alpha]
    result = []
    for i in str1_lst :
        result.append(i)
    for i in str2_lst :
        if i in str1_lst :
            str1_lst.remove(i)
        elif i not in str1_lst :
            result.append(i)
            
    answer2 = len(result)
    if answer1 == 0 and answer2 == 0 :
        answer = 65536
    else :
        answer = math.floor((answer1 / answer2) * 65536)
    return answer