'''
https://programmers.co.kr/learn/courses/30/lessons/77884
'''

def solution(left, right):
    num_dict = {}
    for i in range(left, right + 1) :   # left부터 right 까지
        n = 0                           # 약수의 수
        for j in range(1, i + 1) :      # 약수 찾기
            if i % j == 0 :
                n += 1
        num_dict[i] = n

    answer = 0
    for key, value in num_dict.items() :
        if value % 2 == 0 :              # 약수의 갯수가 짝수일 경우
            answer += key                # 더하기
        else :                              
            answer -= key                # 반대의 경우 빼주
        
    return answer