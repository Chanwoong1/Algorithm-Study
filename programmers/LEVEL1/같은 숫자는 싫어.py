'''
https://programmers.co.kr/learn/courses/30/lessons/12906
'''

def solution(arr):
    answer = []
    for i in range(len(arr)) :
        if i > 0 and arr[i-1] == arr[i] :   # 직전 수랑 같으면 무시
            pass
        else :
            answer.append(arr[i])           # 다르면 추가
    return answer