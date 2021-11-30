'''
https://programmers.co.kr/learn/courses/30/lessons/12915
'''

def solution(strings, n):
    answer = []
    string_dict = {}
    
    for i in strings :
        string_dict[i[n]] = []  # 정해진 인덱스의 문자로 key 생성
        
    for i in strings :
        string_dict[i[n]].append(i)                     # value 추가
        string_dict[i[n]] = sorted(string_dict[i[n]])   # 기존에 value가 있을 수 있으므로 정렬
    sorted_by_value = sorted(string_dict.items(), key= lambda x: x[0])  # key를 기준으로 정렬
    
    for i in sorted_by_value :
        answer += i[1]  # 문자열 합치기
    return answer