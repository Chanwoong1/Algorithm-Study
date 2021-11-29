'''
https://programmers.co.kr/learn/courses/30/lessons/42862#
'''

def solution(n, lost, reserve):
    answer = n - len(lost)
    students = [x for x in range(1, n + 1)]
    
    remove_student = []
    for i in lost :
        if i in reserve :
            remove_student.append(i)
    answer += len(remove_student)   # 도난당했지만 여벌옷이 있는 학생 수 더해주기
    
    for i in remove_student :   # lost와 reserve에서 제거
        lost.remove(i)
        reserve.remove(i)
    
    for i in students :         # 옆 친구들에게 대여
        if i in lost :
            if i - 1 in reserve :
                answer += 1
                reserve.remove(i - 1)
            elif i + 1 in reserve :
                answer += 1
                reserve.remove(i + 1)
    return answer