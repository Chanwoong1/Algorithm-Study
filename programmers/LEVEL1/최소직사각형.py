'''
https://programmers.co.kr/learn/courses/30/lessons/86491
'''

def solution(sizes):
    width = []
    height = []
    for i, j in sizes :
        if i < j :      # 너비보다 높이가 더 큰 명함이라면
            width.append(j)     # 가로로 눕혀주기
            height.append(i)
        else :
            width.append(i)
            height.append(j)
    answer = max(width) * max(height)
    return answer