'''
https://programmers.co.kr/learn/courses/30/lessons/42840
'''

import numpy as np

def solution(answers):
    a = [1, 2, 3, 4, 5]                 # type 1
    b = [2, 1, 2, 3, 2, 4, 2, 5]        # type 2
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # type 3
    len_answer = len(answers)
    len_a = a * ((len_answer // len(a)) + 1)
    len_a = np.array(len_a[ : len_answer])
    len_b = b * ((len_answer // len(b)) + 1)
    len_b = np.array(len_b[ : len_answer])
    len_c = c * ((len_answer // len(c)) + 1)
    len_c = np.array(len_c[ : len_answer])
    
    a_answer = len([i for i in len_a - np.array(answers) if i == 0])    # 0의 갯수 == 맞은 문제 수
    b_answer = len([i for i in len_b - np.array(answers) if i == 0])
    c_answer = len([i for i in len_c - np.array(answers) if i == 0])
    
    result = []
    ans_dict = {1 : a_answer, 2 : b_answer, 3 : c_answer}
    answer = [a_answer, b_answer, c_answer]
    for key, value in ans_dict.items() :
        if value == max(answer) :   # 가장 많이 맞은 사람 찾기
            result.append(key)
    return result