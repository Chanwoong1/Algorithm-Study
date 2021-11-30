'''
https://programmers.co.kr/learn/courses/30/lessons/68644
'''

def solution(numbers):
    result = []
    for i in range(len(numbers)) :  
        for j in range(len(numbers)) :
            if i > j :  # 중복 없이 두 수를 뽑기 위해
                if numbers[i] + numbers[j] not in result :  # 중복 없이 result에 추가하기 위해
                    result.append(numbers[i] + numbers[j])
    answer = sorted(result)
    return answer