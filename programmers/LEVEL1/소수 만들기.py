'''
https://programmers.co.kr/learn/courses/30/lessons/12977
'''

def solution(nums):
    tmp = []
    result = []
    for i in range(len(nums)) :
        for j in range(1, len(nums)) :
            for k in range(2, len(nums)) :
                if i < j < k :  # 중복 없이 숫자 3개 고르기
                    tmp.append(sum([nums[i], nums[j], nums[k]]))
    tmp = sorted(tmp)
    for i in tmp :  # 소수 찾기
        n = 0
        for j in range(2, i) :
            if i % j == 0 : # 1과 자기 자신을 제외한 수를 나눴을 때 나머지가 0인 경우가 있다면
                n += 1  # 소수가 아니다
        if n == 0 :     # 소수인것만 추가
            result.append(i)
    return len(result)  # 소수 갯수 출력