'''
https://programmers.co.kr/learn/courses/30/lessons/12973
'''

def solution(s):
    answer = 0
    result = []
    for i in list(s) :
        result.append(i)
        if len(result) > 1 and result[-1] == result[-2] :
            result.pop()
            result.pop()
    if len(result) == 0 :
        return 1

    return answer

'''
s를 리스트에 담아 for 문을 돌리면서 result에 하나씩 추가한다.
result에 2개 이상의 값이 들어있을 때, if문의 조건을 만족하면, 만족하는 가장 마지막 값 2개를 빼준다.
모든 작업이 끝난 뒤, result에 아무것도 없다면 1을 반환,
남아있다면 0을 반환하도록 한다.
'''