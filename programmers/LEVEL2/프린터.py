'''
https://programmers.co.kr/learn/courses/30/lessons/42587
'''

def find_max(lst, location) :   # 최댓값을 리스트의 맨 앞으로 보내주는 함수
    tmp = lst.index(max(lst))
    if location < tmp :
        location = location + len(lst[tmp : ])  # 리스트가 변하면서 location도 바뀌니까 그걸 계산해준다.
    else :
        location = location - len(lst[ : tmp])
    return lst[tmp : ] + lst[ : tmp], location

def solution(priorities, location):
    answer = 0
    while location >= 0 :
        priorities, location = find_max(priorities, location)   # 반복 수행
        if max(priorities) == priorities[0] :                   # 맨 앞이 최대값일때 프린트
            priorities.pop(0)                                   
            answer += 1
            location -= 1

    return answer