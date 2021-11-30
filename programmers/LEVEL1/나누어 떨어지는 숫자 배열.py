'''
https://programmers.co.kr/learn/courses/30/lessons/12910
'''

def solution(arr, divisor):
    answer = []
    for i in arr :
        if i % divisor == 0 :   # 나누어 떨어질 때
            answer.append(i)    # 추가
    if len(answer) == 0 :       # 나누어 떨어지는 요소가 하나도 없다면
        return [-1]             # -1을 배열에 담아 반환
    else :
        return sorted(answer)   # 정렬 후 반환