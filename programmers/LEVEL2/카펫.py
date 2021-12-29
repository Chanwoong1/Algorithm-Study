# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    result = []
    answer = []
    tmp = brown + yellow    # 총 면적

    # 세로의 길이 후보 선정
    for i in range(1, round(tmp / 3) + 1) :
        if tmp % i == 0 :
            if tmp // i >= i :
                result.append(i)
    
    # 조건에 맞는 길이 찾아줌
    for i in result :
        other = tmp // i
        if other * 2 + i * 2 - 4 == brown :
            answer.append(other)
            answer.append(i)
    return answer