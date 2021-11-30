'''
https://programmers.co.kr/learn/courses/30/lessons/12950
'''

import numpy as np

def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2) :
        answer.append((np.array(i) + np.array(j)).tolist()) # array로 변환 후 더해준 뒤 다시 리스트로 변환
    return answer