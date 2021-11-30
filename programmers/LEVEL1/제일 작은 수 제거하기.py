'''
https://programmers.co.kr/learn/courses/30/lessons/12935
'''

def solution(arr):
    arr.remove(min(arr))    # 가장 작은 수를 arr에서 제거
    if arr == [] :          # arr이 공백이라면
        return [-1]         # [-1] 출력
    else :
        return arr          # 나머지의 경우 arr 출력