'''
https://programmers.co.kr/learn/courses/30/lessons/42888
'''

def solution(record):
    answer = []
    # step1
    id_dict = {}
    for i in record :
        msg = i.split()
        if msg[0] == 'Enter' :
            id_dict[msg[1]] = msg[2]
        elif msg[0] == 'Change' :
            id_dict[msg[1]] = msg[2]
    # step2
    for i in record :
        msg = i.split()
        if msg[0] == 'Enter' :
            answer.append('{}님이 들어왔습니다.'.format(id_dict[msg[1]]))
        elif msg[0] == 'Leave' :
            answer.append('{}님이 나갔습니다.'.format(id_dict[msg[1]]))
    return answer
