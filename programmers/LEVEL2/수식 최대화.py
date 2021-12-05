'''
https://programmers.co.kr/learn/courses/30/lessons/67257
'''

from itertools import permutations
def dustks(expression, rlgh) :
    i = 0
    while rlgh in expression :
        if expression[i] == rlgh :
            if rlgh == '*' :
                expression[i - 1] = str(int(expression[i - 1]) * int(expression[i + 1]))
                expression.pop(i)
                expression.pop(i)
                i = 0
            elif rlgh == '+' :
                expression[i - 1] = str(int(expression[i - 1]) + int(expression[i + 1]))
                expression.pop(i)
                expression.pop(i)
                i = 0
            else :
                expression[i - 1] = str(int(expression[i - 1]) - int(expression[i + 1]))
                expression.pop(i)
                expression.pop(i)
                i = 0
        else :
            i += 1
    return expression
'''
우선순위 연산하는 함수를 먼저 만들어 주었다.
우선순위로 지정된 기호 먼저 다 없애주는 방식
'''

def solution(expression):
    dict = {'+' : ' + ', '-' : ' - ', '*' : ' * '}
    for key, value in dict.items() :
        expression = expression.replace(key, value)
    expression = expression.split()
    tmp = expression.copy()
    result = []
    lst = []
    if '*' in expression :
        lst.append('*')
    if '-' in expression :
        lst.append('-')
    if '+' in expression :
        lst.append('+')
    for i in permutations(lst) :
        for j in i :
            tmp = dustks(tmp, j)
        result.append(abs(int(tmp[0])))
        tmp = expression.copy()
    return max(result)

'''
dict에 미리 공백을 포함한 연산문자를 넣어둔 뒤, replace를 이용해 변경해주고,
문자간에 생긴 공백을 기준으로 리스트로 쪼개줬다.
그 후, 순열을 이용해 우선순위 리스트를 for문을 돌려가며 값들의 절대값들을 result에 포함시켜주었다.
가장 큰 값을 반환한다.
'''