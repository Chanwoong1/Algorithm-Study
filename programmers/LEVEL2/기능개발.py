'''
https://programmers.co.kr/learn/courses/30/lessons/42586#
'''

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0 :
        if (progresses[0] + time * speeds[0]) >= 100 :  # time을 점점 늘려주면서 100이 되면
            progresses.pop(0)
            speeds.pop(0)
            count += 1  # count 1 증가
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer