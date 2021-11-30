'''
https://programmers.co.kr/learn/courses/30/lessons/17681
'''

def solution(n, arr1, arr2):
    arr1_result = []
    arr2_result = []
    for i, j in zip(arr1, arr2) :
        if len(str(bin(i))[2:]) != n :  # 자릿수가 맞지 않을 때
            arr1_result.append('0' * (n - len(str(bin(i))[2:])) + str(bin(i))[2:])  # 앞자리 공백만큼 0 추가
        else :
            arr1_result.append(str(bin(i))[2:])
        
        if len(str(bin(j))[2:]) != n :
            arr2_result.append('0' * (n - len(str(bin(j))[2:])) + str(bin(j))[2:])
        else :
            arr2_result.append(str(bin(j))[2:])
    
    result = []
    for i, j in zip(arr1_result, arr2_result) :
        tmp = ''
        for k in range(n) :
            if i[k] == '0' and j[k] == '0' :    # 두 지도 다 0일 경우
                tmp += ' '                      # 공백 출력
            else :
                tmp += '#'                      # 나머지 출력
        result.append(tmp)
    return result